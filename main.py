from flask import Flask
from flask_restful import Api
from app.resources.preprocess import Preprocess
from app.resources.cosineSimilarity import CosineSimilarity

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(CosineSimilarity, '/calculate')
api.add_resource(Preprocess, '/preprocess')

if __name__ == "__main__":
    app.run(debug=True)