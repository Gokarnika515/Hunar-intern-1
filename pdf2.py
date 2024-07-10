import fitz  # PyMuPDF
def extract_text_from_first_page(pdf_file):
    # Extract text from the first page of the PDF
    doc = fitz.open(pdf_file)
    page = doc.load_page(0)
    text = page.get_text()
    doc.close()
    return text

def compare_pdf_files(pdf_file1, pdf_file2):
    try:
        # Extract text from the first page of each PDF
        text1 = extract_text_from_first_page(pdf_file1)
        text2 = extract_text_from_first_page(pdf_file2)
        
        # Compare the extracted text
        if text1 != text2:
            print("Textual content is different.")
            return False
        
        # Compare the number of pages
        doc1 = fitz.open(pdf_file1)
        doc2 = fitz.open(pdf_file2)
        
        if len(doc1) != len(doc2):
            print("Number of pages is different.")
            doc1.close()
            doc2.close()
            return False
        
        # Compare the size of each page
        for page_num in range(len(doc1)):
            page1 = doc1.load_page(page_num)
            page2 = doc2.load_page(page_num)
            
            if page1.rect != page2.rect:
                print(f"Page {page_num + 1} size is different.")
                doc1.close()
                doc2.close()
                return False
            
            # Compare the text content of each page (already checked the first page)
            if page_num > 0:
                text1 = page1.get_text()
                text2 = page2.get_text()
                if text1 != text2:
                    print(f"Textual content on page {page_num + 1} is different.")
                    doc1.close()
                    doc2.close()
                    return False
        
        # If all checks pass
        print("PDF files are identical.")
        doc1.close()
        doc2.close()
        return True
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return False

# Example usage:
if __name__ == "__main__":
    pdf_file1 = "file1.pdf"
    pdf_file2 = "file2.pdf"
    
    identical = compare_pdf_files(pdf_file1, pdf_file2)
    if identical:
        print("The PDF files are identical.")
    else:
        print("The PDF files are different.")

