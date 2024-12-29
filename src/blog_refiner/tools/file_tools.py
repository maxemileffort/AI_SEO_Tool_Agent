from crewai_tools import tool
import os

@tool
def read_file(file_path: str) -> str:
    """
    Reads content from DOCX, PDF, or TXT files.
    """
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif ext.lower() == '.docx':
        import docx
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    elif ext.lower() == '.pdf':
        from PyPDF2 import PdfReader
        reader = PdfReader(file_path)
        return ''.join([page.extract_text() for page in reader.pages])
    else:
        return f"Unsupported file format: {ext}"

@tool
def write_file(file_path: str, content: str) -> str:
    """
    Writes content to DOCX, PDF, or TXT files.
    """
    _, ext = os.path.splitext(file_path)
    if ext.lower() == '.txt':
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    elif ext.lower() == '.docx':
        import docx
        doc = docx.Document()
        doc.add_paragraph(content)
        doc.save(file_path)
    elif ext.lower() == '.pdf':
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)
        pdf.output(file_path)
    else:
        return f"Unsupported file format: {ext}"
    return f"File written successfully to {file_path}"
