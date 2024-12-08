import nltk
import re
import json

from flask import request
from flask_restful import Resource
from app.utils.utils import documentUpload, extract_text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')

class Preprocess(Resource):
    def post(self):
        # Upload file
        upload = documentUpload(request.files)
        if upload == False:
            return {"message": "Gagal mengupload file"}

        # Ekstrak teks
        file_path = upload['file_path']
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
        unique_tokens = list(dict.fromkeys(filtered_tokens))
        stemmed_text = stemmer.stem(' '.join(unique_tokens))

        return {"message": json.dumps(stemmed_text)}

        
    