import os
import time
import pdfplumber

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

def documentUpload(files):
    # Buat folder upload jika belum ada
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if 'file' not in files:
        return False
    
    file = files['file']

    if file.filename == '':
        return False
    
    # Membuat nama file
    file_ext = os.path.splitext(file.filename)[1]
    epoch_time = int(time.time()) 
    new_filename = f"{epoch_time}{file_ext}"

    # Simpan file ke folder uploads dengan nama yang sudah dibuat
    file_path = os.path.join(UPLOAD_FOLDER, new_filename)
    file.save(file_path)

    return {"file_path": file_path}

def extract_text(path):
    text = ''
    
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text