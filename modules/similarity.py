import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(texts):
    # Menghitung cosine similarity dari kumpulan teks
    vectorizer = TfidfVectorizer(ngram_range=(2, 3))
    tfidf_matrix = vectorizer.fit_transform(texts)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    return similarity_matrix.tolist()
