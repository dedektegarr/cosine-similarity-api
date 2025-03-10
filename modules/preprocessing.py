import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Unduh stopwords jika belum ada
nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")

# Inisialisasi Stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
stop_words = set(stopwords.words("indonesian"))

def preprocess_text(text):
    """ Melakukan preprocessing pada teks """
    text = text.lower()  # Case folding

    text = re.sub(r'\d+', '', text)  # Hapus angka
    text = re.sub(r'\W+', ' ', text) # Hapus simbol
    text = text.translate(str.maketrans("", "", string.punctuation))  # Hapus tanda baca

    words = word_tokenize(text)  # Tokenizing
    words = [word for word in words if word not in stop_words]  # Stopword Removal
    words = [stemmer.stem(word) for word in words]  # Stemming

    return " ".join(words)

