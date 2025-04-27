import os
import re
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# Configuration
input_folder = "your_folder_here"
output_folder = input_folder  # or change if you want to move renamed files elsewhere
max_words = 5
tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Change if needed
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

# Helper: Sanitize filename
def sanitize_filename(s):
    s = re.sub(r'[^\w\s-]', '', s)  # Remove non-word characters
    s = re.sub(r'\s+', '_', s)      # Replace spaces with underscores
    return s.strip('_')

# Helper: Extract text
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text = page.get_text()
        if text.strip():
            break
    doc.close()
    return text

# Helper: OCR if no text found
def ocr_text(pdf_path):
    images = convert_from_path(pdf_path, dpi=300)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
        if text.strip():
            break
    return text

# Main logic
def rename_pdfs(folder):
    pdf_files = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]
    for idx, pdf_file in enumerate(pdf_files, start=1):
        pdf_path = os.path.join(folder, pdf_file)

        # Try extracting text
        text = extract_text(pdf_path)
        if not text.strip():
            print(f"No text found in {pdf_file}. Running OCR...")
            text = ocr_text(pdf_path)

        if not text.strip():
            print(f"Skipping {pdf_file}, no text found even after OCR.")
            continue

        # Get first 5 words
        words = text.strip().split()
        selected_words = words[:max_words]
        base_name = sanitize_filename(' '.join(selected_words))

        # Add enumeration to filename
        new_filename = f"{base_name}_{idx}.pdf"
        new_path = os.path.join(output_folder, new_filename)

        # Rename the file
        os.rename(pdf_path, new_path)
        print(f"Renamed '{pdf_file}' to '{new_filename}'")

if __name__ == "__main__":
    rename_pdfs(input_folder)
