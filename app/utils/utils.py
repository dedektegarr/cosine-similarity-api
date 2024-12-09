import os
import nltk
import time
import re
import glob
import json
import pdfplumber

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

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

def is_valid_pdf(path):
    try:
        with open(path, 'rb') as file:
            parser = PDFParser(file)
            PDFDocument(parser)  # Jika berhasil, maka file valid
        return True
    except:
        return False

def is_json_exists(pdf_path, output_folder):
    file_name = os.path.basename(pdf_path).replace('.pdf', '.json')
    output_path = os.path.join(output_folder, file_name)
    return os.path.exists(output_path)

def search_json_file(name):
        # Folder untuk menyimpan hasil proses
        output_folder = 'processed_text'
        filename = name.replace('.pdf', '.json')

        # Mencari file JSON berdasarkan nama
        json_files = glob.glob(f"{output_folder}/{filename}")
        
        if not json_files:
            return f"No file found with name {filename}.json"
        
        # Membaca konten file JSON jika ditemukan
        result = ""
        for file_path in json_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                result = json.load(file)

        return result

def preprocessDocument(path):
    # Ekstrak teks
    file_path = path
    text = extract_text(file_path)

    # Hapus angka dan simbol yang tidak relevan
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\W+', ' ', text)
    
    # Tokenizing (pemecahan menjadi kata)
    tokens = word_tokenize(text)

    # Filtering Stop Words (penghapusan kata tidak penting)
    stop_words = set(stopwords.words('indonesian'))
    filtered_tokens = [word for word in tokens if len(word) > 2 if word.isalnum() and word not in stop_words]

    # Stemming (penghilangan imbuhan / Indonesian stemming)
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stemmed_text = stemmer.stem(' '.join(filtered_tokens))

    return stemmed_text