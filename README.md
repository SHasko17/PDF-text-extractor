PDF to Text OCR Processor

Overview

This project extracts text from a PDF file using Optical Character Recognition (OCR). It converts each page into an image, processes the images in parallel using pytesseract, and writes the extracted text to an output file.

Features

Converts PDF pages to images using pdf2image.

Uses pytesseract for OCR-based text extraction.

Processes pages in chunks using ThreadPoolExecutor for efficient multi-threading.

Outputs extracted text in a structured format.

Prerequisites

Ensure you have the following dependencies installed before running the script:

Required Python Packages:

Install dependencies using:

pip install pytesseract pdf2image Pillow

Additional Requirements:

Tesseract OCR: Ensure Tesseract is installed on your system.

Windows: Download from here

Linux/macOS: Install using package manager, e.g.,

sudo apt install tesseract-ocr  # Ubuntu/Debian
brew install tesseract          # macOS

Poppler: Required for pdf2image to function properly.

Windows: Download from here

Linux/macOS: Install using package manager, e.g.,

sudo apt install poppler-utils  # Ubuntu/Debian
brew install poppler            # macOS

Usage

Run the script by specifying the PDF file path and other parameters:

process_pdf_in_chunks('path/to/pdf_file.pdf', chunk_size=5, dpi=500, output_file='output.txt')

Parameters:

pdf_path: Path to the input PDF file.

chunk_size: Number of pages to process concurrently.

dpi: Resolution of converted images (higher DPI improves accuracy but increases processing time).

output_file: Path to save the extracted text.

Example Execution

python script.py

This will process Images/DanKiralyiKonyvtar.pdf in chunks of 5 pages at 500 DPI and store the output in DanKiralyiKonyvtar-OUT.txt.

Output Format

The output text file will be structured as follows:

Page 1:
Extracted text from page 1...

Page 2:
Extracted text from page 2...

Troubleshooting

If Tesseract is not found, ensure it's installed and added to your system's PATH.

If the PDF is not processed correctly, try lowering the DPI or chunk size.
