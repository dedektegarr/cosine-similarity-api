import json

from flask import request
from flask_restful import Resource
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CosineSimilarity(Resource):
    def post(self):
        if "word_tokens" not in request.json or not request.json["word_tokens"]:
            return {"message": "Masukkan word token"}, 400
        
        word_tokens = json.loads(request.json["word_tokens"])

        vectorizer = TfidfVectorizer(ngram_range=(2,3))
        matrix = vectorizer.fit_transform(word_tokens)
        result = cosine_similarity(matrix[0], matrix)

        return {"message": result[0].tolist()}
    