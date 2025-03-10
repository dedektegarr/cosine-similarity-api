from flask import Flask, request, jsonify
from modules.preprocessing import preprocess_text
from modules.similarity import calculate_cosine_similarity

app = Flask(__name__)

@app.route("/api/preprocess", methods=["POST"])
def preprocess():
    data = request.get_json()
    if not data or "text" not in data or not data["text"].strip():
        return jsonify({"error": "Text tidak boleh kosong"}), 400
    
    processed_text = preprocess_text(data["text"])
    return jsonify({"processed_text": processed_text})

@app.route("/api/similarity", methods=["POST"])
def similarity():
    data = request.get_json()
    if not data or "texts" not in data:
        return jsonify({"error": "Texts tidak boleh kosong"}), 400
    
    similarity_matrix = calculate_cosine_similarity(data["texts"])
    return jsonify({"similarity_matrix": similarity_matrix})

if __name__ == "__main__":
    app.run(debug=True)
