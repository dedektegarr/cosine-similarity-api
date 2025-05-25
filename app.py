from flask import Flask, request, jsonify
from modules.preprocessing import preprocess_text
from modules.similarity import calculate_cosine_similarity

app = Flask(__name__)

@app.route("/api/preprocess", methods=["POST"])
def preprocess():
    data = request.get_json()
    if not data or "texts" not in data or not isinstance(data["texts"], list):
        return jsonify({"error": "Texts tidak boleh kosong dan harus berupa array"}), 400
    
    processed_texts = [preprocess_text(text) for text in data["texts"]]
    return jsonify({"preprocessed_texts": processed_texts})

@app.route("/api/similarity", methods=["POST"])
def similarity():
    data = request.get_json()
    if not data or "texts" not in data or not isinstance(data["texts"], list):
        return jsonify({"error": "Texts tidak boleh kosong dan harus berupa array"}), 400
    
    similarity_matrix = calculate_cosine_similarity(data["texts"])
    return jsonify({"similarity_matrixss": similarity_matrix})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
