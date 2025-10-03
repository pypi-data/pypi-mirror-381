import torch
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
from PIL import Image
import matplotlib.pyplot as plt
import fitz  # PyMuPDF
import torchvision.transforms as T
import os
import camelot
import pandas as pd
import re
import tempfile
import subprocess
import sys
import json

# You will need to install pytesseract and Google's Tesseract-OCR engine
# pip install pytesseract
# Installation instructions for Tesseract: https://github.com/tesseract-ocr/tesseract
import pytesseract

# --- Global Configuration & Model Loading ---

# This list MUST match the labels discovered during training.
DISCOVERED_LABELS = sorted([
    'PID', 'Supplemental Specifications', 'Sheet Index', 'FAN',
    'Standard Construction Drawings', 'Special Provisions'
])

# Use GPU if available
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def get_model(num_classes):
    """
    Defines the Faster R-CNN model architecture.
    This must be identical to the function in your training script.
    """
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights=None)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    return model


def load_trained_model(model_path):
    """
    Loads the trained model weights and prepares it for inference.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    print(f"Using device: {DEVICE}")
    num_classes = len(DISCOVERED_LABELS) + 1  # +1 for the background class

    model = get_model(num_classes)
    model.load_state_dict(torch.load(model_path, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()  # Set the model to evaluation mode
    print("Model loaded successfully!")
    return model


# --- Step 1: Finder Functions ---

def find_section_in_pdf(model, pdf_path, target_label, page_number=1):
    """
    Finds a labeled section in a PDF and returns its coordinates and related info.
    This function performs inference but does not display output.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found at {pdf_path}")
        return None

    doc = fitz.open(pdf_path)
    page_index = page_number - 1
    if not (0 <= page_index < len(doc)):
        print(f"Error: Page {page_number} is invalid. PDF has {len(doc)} pages.")
        doc.close()
        return None

    page = doc[page_index]
    # Render at a higher DPI for better OCR results
    pix = page.get_pixmap(dpi=300)
    # Store the original PDF page dimensions for coordinate conversion
    page_dimensions = (page.rect.width, page.rect.height)
    doc.close()

    original_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Use the generalized image finder for the core model inference
    info = find_section_in_image(model, original_image, target_label)
    if info:
        info["page_dimensions"] = page_dimensions
        info["page_number"] = page_number
    return info


def find_section_in_image(model, image_obj_or_path, target_label):
    """
    Finds a labeled section in an image and returns a dictionary of information.
    """
    if isinstance(image_obj_or_path, str):
        if not os.path.exists(image_obj_or_path):
            print(f"Error: Image file not found at {image_obj_or_path}")
            return None
        original_image = Image.open(image_obj_or_path).convert("RGB")
    else:  # Assumes it's a PIL Image object
        original_image = image_obj_or_path

    id2label = {i + 1: name for i, name in enumerate(DISCOVERED_LABELS)}

    transform = T.ToTensor()
    img_tensor = transform(original_image).to(DEVICE)

    with torch.no_grad():
        prediction = model([img_tensor])[0]

    best_box, best_score = None, 0.0
    for score, label_id, box in zip(prediction["scores"], prediction["labels"], prediction["boxes"]):
        if label_id.item() in id2label and id2label[label_id.item()] == target_label:
            if score > best_score:
                best_score, best_box = score, box.cpu().numpy()

    if best_box is not None:
        print(f"Found '{target_label}' with confidence {best_score:.4f}")
        return {
            "best_box": best_box,
            "best_score": best_score,
            "original_image": original_image
        }
    else:
        print(f"Could not find a bounding box for '{target_label}'.")
        return None


# --- Step 2: Data Extraction Functions ---

def ocr_image_table_to_dataframe(image_obj: Image.Image) -> pd.DataFrame:
    """
    Performs OCR on a PIL Image object containing a table and reconstructs
    it into a pandas DataFrame.
    """
    print("🤖 Starting structured OCR on image...")
    try:
        ocr_data = pytesseract.image_to_data(
            image_obj,
            output_type=pytesseract.Output.DATAFRAME
        )
    except pytesseract.TesseractNotFoundError:
        print("\n--- OCR ERROR: Tesseract is not installed or not in your PATH. ---")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred during OCR: {e}")
        return pd.DataFrame()

    ocr_data = ocr_data[ocr_data.conf > -1]
    ocr_data.dropna(subset=['text'], inplace=True)
    ocr_data['text'] = ocr_data['text'].str.strip()
    ocr_data = ocr_data[ocr_data.text != '']

    if ocr_data.empty:
        print("ℹ️ OCR did not detect any text in the image region.")
        return pd.DataFrame()

    grouped = ocr_data.groupby(['block_num', 'par_num', 'line_num'])
    table_rows = []
    for (block, par, line), words in grouped:
        line_text = ' '.join(words.sort_values('left')['text'])
        table_rows.append(line_text.split())

    max_cols = max(len(row) for row in table_rows) if table_rows else 0
    padded_rows = [row + [None] * (max_cols - len(row)) for row in table_rows]

    if not padded_rows:
        print("ℹ️ Could not reconstruct a table from the OCR data.")
        return pd.DataFrame()

    df = pd.DataFrame(padded_rows)

    if not df.empty:
        print(f"✅ OCR successfully extracted a table with {df.shape[0]} rows and {df.shape[1]} columns.")

    return df


def extract_table_or_text(pdf_path, bounding_box_info):
    """
    Uses a bounding box to extract a table with Camelot. If it fails,
    it falls back to extracting a structured table with OCR.
    """
    if not bounding_box_info or bounding_box_info.get("best_box") is None:
        print("Error: Invalid bounding_box_info provided.")
        return None

    best_box = bounding_box_info["best_box"]
    original_image = bounding_box_info["original_image"]
    page_dims = bounding_box_info["page_dimensions"]
    page_num = bounding_box_info["page_number"]

    xmin_pix, ymin_pix, xmax_pix, ymax_pix = best_box
    img_width, img_height = original_image.size
    pdf_page_width, pdf_page_height = page_dims

    y_expansion_up = 150;
    y_expansion_down = 400;
    x_expansion = 50
    ymin_pix_exp = max(0, ymin_pix - y_expansion_up)
    ymax_pix_exp = min(img_height, ymax_pix + y_expansion_down)
    xmin_pix_exp = max(0, xmin_pix - x_expansion)
    xmax_pix_exp = min(img_width, xmax_pix + x_expansion)

    pdf_x1 = xmin_pix_exp * (pdf_page_width / img_width)
    pdf_x2 = xmax_pix_exp * (pdf_page_width / img_width)
    pdf_y1_from_top = ymin_pix_exp * (pdf_page_height / img_height)
    camelot_y1 = pdf_page_height - pdf_y1_from_top
    camelot_y2 = pdf_page_height - (ymax_pix_exp * (pdf_page_height / img_height))
    table_area_str = f"{pdf_x1},{camelot_y1},{pdf_x2},{camelot_y2}"

    print(f"\nAttempting table extraction in area: {table_area_str} on page {page_num}")

    cropped_image = original_image.crop((xmin_pix_exp, ymin_pix_exp, xmax_pix_exp, ymax_pix_exp))

    try:
        tables = camelot.read_pdf(pdf_path, pages=str(page_num), flavor='stream', table_areas=[table_area_str])
        if tables.n > 0:
            print("✅ Camelot found a table. PDF is likely text-based in this region.")
            return {"type": "camelot_table", "data": tables[0].df, "image": cropped_image}
        else:
            print("ℹ️ Camelot did not find a table. Attempting structured OCR...")
            ocr_df = ocr_image_table_to_dataframe(cropped_image)
            if not ocr_df.empty:
                return {"type": "ocr_table", "data": ocr_df, "image": cropped_image}
            else:
                print("❌ Both Camelot and structured OCR failed.")
                return None
    except Exception as e:
        print(f"An error occurred during Camelot extraction: {e}. Falling back to OCR.")
        ocr_df = ocr_image_table_to_dataframe(cropped_image)
        if not ocr_df.empty:
            return {"type": "ocr_table", "data": ocr_df, "image": cropped_image}
        return None


# --- Step 3: Display and Debug Functions ---
def display_croppped_section(bounding_box_info, target_label):
    if not bounding_box_info or bounding_box_info.get("best_box") is None:
        print("Cannot display results: Invalid bounding_box_info provided.")
        return
    original_image = bounding_box_info["original_image"]
    best_box = bounding_box_info["best_box"]
    fig, axs = plt.subplots(1, 2, figsize=(20, 10))
    axs[0].imshow(original_image)
    axs[0].set_title("Original Image");
    axs[0].axis('off')
    xmin, ymin, xmax, ymax = best_box
    expansion_pixels = 30
    img_width, img_height = original_image.size
    xmin = max(0, xmin - expansion_pixels);
    ymin = max(0, ymin - expansion_pixels)
    xmax = min(img_width, xmax + expansion_pixels)
    cropped_image = original_image.crop((xmin, ymin, xmax, ymax))
    axs[1].imshow(cropped_image)
    axs[1].set_title(f"Cropped: '{target_label}'");
    axs[1].axis('off')
    plt.tight_layout();
    plt.show()


# --- Step 4: Main Processing Logic ---

def process_document(model, file_path, target_label, page_number=1):
    """
    Main orchestrator. Determines file type and routes to the correct functions.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}");
        return None

    file_extension = os.path.splitext(file_path)[1].lower()
    is_pdf = file_extension == '.pdf'
    is_image = file_extension in ['.png', '.jpg', '.jpeg', '.tiff', '.tif']

    if is_pdf:
        print(f"--- Processing PDF: {file_path} ---")
        section_info = find_section_in_pdf(model, file_path, target_label, page_number=page_number)
        if not section_info: return None
        return extract_table_or_text(file_path, section_info)

    elif is_image:
        print(f"--- Processing Image: {file_path} ---")
        section_info = find_section_in_image(model, file_path, target_label)
        if not section_info: return None

        print("ℹ️ Input is an image. Bypassing Camelot for direct structured OCR.")
        best_box = section_info["best_box"];
        original_image = section_info["original_image"]
        img_width, img_height = original_image.size

        xmin_pix, ymin_pix, xmax_pix, ymax_pix = best_box
        y_exp_up = 150;
        y_exp_down = 400;
        x_exp = 50
        ymin_pix_exp = max(0, ymin_pix - y_exp_up);
        ymax_pix_exp = min(img_height, ymax_pix + y_exp_down)
        xmin_pix_exp = max(0, xmin_pix - x_exp);
        xmax_pix_exp = min(img_width, xmax_pix + x_exp)

        cropped_for_ocr = original_image.crop((xmin_pix_exp, ymin_pix_exp, xmax_pix_exp, ymax_pix_exp))
        ocr_df = ocr_image_table_to_dataframe(cropped_for_ocr)

        if not ocr_df.empty:
            return {"type": "ocr_table_from_image", "data": ocr_df, "image": cropped_for_ocr}
        else:
            print("❌ Structured OCR failed to find a table in the image.")
            return None
    else:
        print(f"Error: Unsupported file format '{file_extension}'.")
        return None


# --- Step 5: Data Cleaning and Export ---

def open_file(filepath):
    """Cross-platform way to open a file."""
    if sys.platform == "win32":
        os.startfile(filepath)
    elif sys.platform == "darwin":  # macOS
        subprocess.run(["open", filepath], check=True)
    else:  # linux
        subprocess.run(["xdg-open", filepath], check=True)


def pre_clean_ocr_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies regex filters to a raw OCR DataFrame to remove obvious garbage,
    while preserving the table's original structure for review.
    """
    if raw_df.empty:
        return pd.DataFrame()

    print("🧹 Pre-cleaning raw OCR data before exporting to Excel...")

    # Define regex for codes (e.g., BP-3.1) and dates (e.g., 07-16-04)
    code_pattern = r'[A-Z]{1,3}[-]?[\d\.-]+M?'
    date_pattern = r'\d{2}[-]\d{2}[-]\d{2}'

    # Create a new DataFrame of the same size, filled with NaN to store results
    cleaned_df = pd.DataFrame(index=raw_df.index, columns=raw_df.columns)

    for r_idx, row in raw_df.iterrows():
        for c_idx, item in row.items():
            if pd.isna(item):
                continue

            cell_content = str(item).replace('—', '-')

            # Use findall to extract all parts that match the patterns
            valid_codes = re.findall(code_pattern, cell_content)
            valid_dates = re.findall(date_pattern, cell_content)

            all_valid_parts = valid_codes + valid_dates

            if all_valid_parts:
                # Reconstruct the cell content with only the valid parts
                cleaned_df.loc[r_idx, c_idx] = ' '.join(all_valid_parts)

    return cleaned_df


def export_for_review(result: dict):
    """
    Pre-cleans the OCR data, saves the cleaned DataFrame to Excel and the
    cropped image to a file, then opens both for manual user review.
    """
    if not result or 'data' not in result or 'image' not in result:
        print("Export function received invalid input.")
        return

    raw_df = result['data']
    cropped_image = result['image']

    # Pre-clean the data to give the user a better starting point
    cleaned_for_review_df = pre_clean_ocr_data(raw_df)

    print("\n" + "---" * 10)
    print("✨ Exporting pre-cleaned data for manual review...")

    try:
        # Create temp files that won't be deleted immediately
        image_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        excel_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')

        # Save the data
        cropped_image.save(image_file.name)
        # Save the PRE-CLEANED, multi-column DataFrame without a header
        cleaned_for_review_df.to_excel(excel_file.name, index=False, header=False)

        # Close the files to ensure they are written to disk
        image_file.close()
        excel_file.close()

        print("\n--- OUTPUTS FOR REVIEW ---")
        print(f"🖼️  Image:      {image_file.name}")
        print(f"📊 Excel:      {excel_file.name}")
        print("\nACTION REQUIRED: Please open the Excel file, clean the data, and save your changes.")
        print("Once saved, run this script again with the path to the cleaned Excel file to generate the final JSON.")

        # Open the two files for immediate review
        print("\n🚀 Opening files for review...")
        open_file(image_file.name)
        open_file(excel_file.name)

    except Exception as e:
        print(f"\n--- ERROR ---")
        print(f"Could not save or open the output files for review: {e}")


def _clean_and_pair_from_df(df: pd.DataFrame) -> dict:
    """
    Internal helper to take a DataFrame, clean it, and return a paired dictionary.
    This is the core data structuring logic.
    """
    if df.empty:
        return {}

    code_pattern = re.compile(r'^[A-Z]{1,3}[-]?[\d\.-]+M?$')
    date_pattern = re.compile(r'^\d{2}[-]\d{2}[-]\d{2}$')

    all_items = []
    for item in df.to_numpy().flatten():
        if pd.notna(item):
            cleaned_item = str(item).replace('—', '-')
            all_items.extend(cleaned_item.split())

    structured_list = []
    i = 0
    while i < len(all_items) - 1:
        current_item, next_item = all_items[i], all_items[i + 1]
        if code_pattern.match(current_item) and date_pattern.match(next_item):
            structured_list.append({"drawing_label": current_item, "effective_date": next_item})
            i += 2
        else:
            i += 1

    return {item['drawing_label']: item['effective_date'] for item in structured_list}


def convert_excel_to_json(excel_path: str, save_and_open: bool = True):
    """
    Reads a user-cleaned Excel file and generates a clean JSON object.
    Can optionally save and open the file or return the dictionary.
    """
    try:
        df = pd.read_excel(excel_path, header=None)
        json_output_dict = _clean_and_pair_from_df(df)

        if not json_output_dict:
            print("Could not extract any valid pairs from the Excel file.")
            return {}

        if save_and_open:
            print("\n--- CONVERSION MODE ---")
            print(f"Reading corrected data from: {excel_path}")
            json_output_path = os.path.splitext(excel_path)[0] + "_final.json"
            with open(json_output_path, 'w', encoding='utf-8') as f:
                json.dump(json_output_dict, f, indent=4)
            print(f"✅ Successfully converted Excel to JSON. Found {len(json_output_dict)} pairs.")
            print(f"Final JSON saved to: {json_output_path}")
            print("🚀 Opening final JSON file...")
            open_file(json_output_path)

        return json_output_dict

    except FileNotFoundError:
        print(f"Error: Excel file not found at {excel_path}")
        return {}
    except Exception as e:
        print(f"An error occurred during Excel to JSON conversion: {e}")
        return {}

def extract_drawing_data(file_path: str, model_path: str, target_label: str = None) -> dict:
    """
    Main importable function to run the extraction workflow on a single file.

    This function processes a PDF, image, or pre-cleaned Excel file and returns
    the extracted drawing data in a structured dictionary format.

    Args:
        file_path (str): The full path to the input file (PDF, image, or Excel).
        model_path (str): The full path to the trained model file.
        target_label (str, optional): A specific label to extract. If None,
                                      the function will search for all known labels.

    Returns:
        dict: A dictionary containing the extracted data. If multiple labels are
              processed, the keys are the labels. Returns an empty dict on failure.
    """
    file_extension = os.path.splitext(file_path)[1].lower()

    # --- Mode 1: Convert a pre-cleaned Excel file ---
    if file_extension in ['.xlsx', '.xls']:
        print(f"--- Running in Conversion Mode for: {file_path} ---")
        # In this mode, the function returns the final, clean JSON structure
        return convert_excel_to_json(file_path, save_and_open=False)

    # --- Mode 2: Extract from a PDF or Image file ---
    elif file_extension in ['.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.tif']:
        print(f"--- Running in Extraction Mode for: {file_path} ---")
        if not os.path.exists(model_path):
            print(f"Error: Model file not found at: {model_path}")
            return {}

        model = load_trained_model(model_path)

        labels_to_process = []
        if target_label:
            if target_label in DISCOVERED_LABELS:
                labels_to_process.append(target_label)
            else:
                print(f"Warning: Label '{target_label}' is not in the list of known labels.")
                return {target_label: "Label not found"}
        else:
            # If no label is specified, process all of them
            labels_to_process = DISCOVERED_LABELS

        all_results = {}
        for label in labels_to_process:
            print(f"\nProcessing Label: '{label}'")
            # process_document finds the section and returns the raw OCR DataFrame
            extracted_result = process_document(model, file_path, label)

            if extracted_result and 'data' in extracted_result and not extracted_result['data'].empty:
                # This workflow cleans the raw data and returns the final paired dictionary
                cleaned_data = _clean_and_pair_from_df(extracted_result['data'])
                all_results[label] = cleaned_data
            else:
                all_results[label] = "No data found"

        return all_results

    # --- Handle unsupported files ---
    else:
        print(f"Error: Unsupported file format in file path: {file_extension}")
        return {}


if __name__ == '__main__':
    # --- CONFIGURATION ---
    # This block now demonstrates how to use the importable function.
    MODEL_PATH = "path/to/your/trained_model.pth"
    INPUT_FILE_PATH = "path/to/your/document.tiff"

    # --- CHOOSE A LABEL ---
    # Set to a specific label like "Standard Construction Drawings" to run only one.
    # Set to None to run all labels in DISCOVERED_LABELS.
    TARGET_LABEL = None

    # --- EXECUTION ---
    if not os.path.exists(INPUT_FILE_PATH):
        print(f"Error: Input file not found at '{INPUT_FILE_PATH}'")
    else:
        # Call the main logic function
        final_data = extract_drawing_data(
            file_path=INPUT_FILE_PATH,
            model_path=MODEL_PATH,
            target_label=TARGET_LABEL
        )

        # --- DISPLAY RESULTS ---
        if final_data:
            print("\n" + "=" * 50)
            print("✅ EXTRACTION COMPLETE. FINAL DATA:")
            print(json.dumps(final_data, indent=4))
            print("=" * 50)

            # Optional: Save the final data to a file
            output_filename = os.path.splitext(os.path.basename(INPUT_FILE_PATH))[0] + "_output.json"
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(final_data, f, indent=4)
            print(f"\nResults also saved to: {output_filename}")