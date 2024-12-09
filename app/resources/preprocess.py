import json
import glob
import os

from flask import request
from flask_restful import Resource
from app.utils.utils import documentUpload, preprocessDocument, is_valid_pdf, is_json_exists, search_json_file

class Preprocess(Resource):
    def get(self):
        filename = request.args.get('filename', '')

        if filename:
            result = search_json_file(filename)

            return {"word_tokens": result}
        
        else:
            pdf_paths = glob.glob('uploads/**/*.pdf', recursive=True)

            # Folder untuk menyimpan hasil proses
            output_folder = 'processed_text'
            os.makedirs(output_folder, exist_ok=True)

            for path in pdf_paths:
                if is_json_exists(path, output_folder):
                    print(f"Skipping {path}, JSON file already exists.")
                    continue

                if not is_valid_pdf(path):
                    print(f"Skipping invalid PDF: {path}")
                    continue  # Skip file jika tidak valid

                processed_text = preprocessDocument(path)

                # Pertahankan nama file dengan mengganti ekstensi menjadi .json
                file_name = os.path.basename(path).replace('.pdf', '.json')
                output_path = os.path.join(output_folder, file_name)

                # Simpan hasil ke file JSON
                with open(output_path, 'w', encoding='utf-8') as json_file:
                    json.dump(processed_text, json_file, indent=4)

            return {"message": pdf_paths}

    def post(self):
        # Upload file
        upload = documentUpload(request.files)
        if upload == False:
            return {"message": "Gagal mengupload file"}

        result = preprocessDocument(upload['file_path'])

        return {"message": json.dumps(result)}

        
    