from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor, as_completed

print("Starting PDF processing...")

def process_page(page, page_number, total_pages):
    print(f"Processing page {page_number + 1} of {total_pages}")
    text = pytesseract.image_to_string(page)
    return page_number, text

def process_pdf_in_chunks(pdf_path, chunk_size, dpi, output_file):
    try:
        # Get total number of pages in the PDF
        pages = convert_from_path(pdf_path, dpi=dpi)
        total_pages = len(pages)
        print(f"Total number of pages in the PDF: {total_pages}")

        # Process the PDF in chunks
        with ThreadPoolExecutor() as executor:
            futures = []
            for start in range(0, total_pages, chunk_size):
                end = min(start + chunk_size, total_pages)
                print(f"Processing pages {start + 1} to {end}...")
                chunk = pages[start:end]

                for page_number, page in enumerate(chunk, start=start):
                    futures.append(executor.submit(process_page, page, page_number, total_pages))

            results = []
            for future in as_completed(futures):
                page_number, text = future.result()
                results.append((page_number, text))

            # Sort results by page number
            results.sort(key=lambda x: x[0])

            # Write results to output file
            with open(output_file, 'a', encoding='utf-8') as f:
                for page_number, text in results:
                    f.write(f"Page {page_number + 1}:\n{text}\n\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Convert and process PDF in chunks
process_pdf_in_chunks('Images/DanKiralyiKonyvtar.pdf', 5, 500, 'DanKiralyiKonyvtar-OUT.txt')