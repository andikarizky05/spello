import pdfplumber
import docx
import io

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()

    if file_type == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_type == 'docx':
        return extract_text_from_docx(uploaded_file)
    else:
        return "❌ Format file tidak didukung."

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(file):
    doc = docx.Document(io.BytesIO(file.read()))
    fullText = [para.text for para in doc.paragraphs]
    return '\n'.join(fullText).strip()
