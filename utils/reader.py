import fitz  # PyMuPDF
import docx

def read_document(file_path):  # <-- aqui é o nome que deve bater com o import
    if file_path.lower().endswith(".pdf"):
        return extract_pdf_text(file_path)
    elif file_path.lower().endswith(".docx"):
        return extract_docx_text(file_path)
    elif file_path.lower().endswith(".txt"):
        return extract_txt(file_path)
    else:
        return "Formato não suportado."

def extract_pdf_text(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])

def extract_docx_text(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
