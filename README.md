PDF Renamer Based on First 5 Words (with OCR Support)

This Python script automatically renames all PDF files in a selected folder based on the first 5 words found in the PDF content.
It intelligently uses text extraction first and OCR fallback (for scanned PDFs) if needed.
Each file is enumerated to ensure unique filenames.


---

Features

Extracts the first 5 meaningful words from each PDF.

Falls back to OCR using Tesseract if no text is found.

Automatically sanitizes filenames (no special characters or spaces).

Enumerates files to avoid naming collisions (_1, _2, _3, etc.).

Simple configuration for input and output folders.

Supports both text PDFs and scanned image PDFs.



---

Installation

1. Clone the repository:

git clone https://github.com/jedisecx/mass-pdf-renamer.git


2. Install required Python libraries:

pip install pymupdf pytesseract pdf2image pillow

3. Install Tesseract OCR:

Download from Tesseract OCR GitHub

Install and make sure to update the tesseract_cmd path in the script if needed.



---

Usage

1. Open mass-pdf-renamer.py.


2. Set your target folder by updating:



input_folder = "your_folder_here"

3. Run the script:



python mass-pdf-renamer.py

4. The PDFs will be renamed inside the specified folder.




---

Example

Before:

- document1.pdf
- file2.pdf
- scan3.pdf

After:

- Introduction_to_Quantum_Mechanics_1.pdf
- Financial_Report_Q1_2023_2.pdf
- Meeting_Notes_Scanned_3.pdf


---

Configuration


---

Notes

If a PDF has no extractable text, OCR will kick in automatically.

Filenames are sanitized to remove special characters and spaces.

Enumeration ensures no two files overwrite each other.

Works with multi-page PDFs (only scans the first page for text).



---

License

This project is licensed under the MIT License.


---

Credits

PyMuPDF for PDF text extraction

pytesseract for OCR

pdf2image for PDF to image conversion

Tesseract OCR


