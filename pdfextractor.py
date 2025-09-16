from pypdf import PdfReader
def text_extractor(file_path):
    pdf_file=PdfReader(file_path)
    pdf_text=" "
    for page in pdf_file.pages:
        pdf_text+=page.extract_text()       

    return pdf_text