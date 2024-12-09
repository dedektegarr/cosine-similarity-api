from flask import Flask
from flask_restful import Api
from app.resources.preprocess import Preprocess
from app.resources.cosineSimilarity import CosineSimilarity

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(CosineSimilarity, 'api/cosim/calculate')
api.add_resource(Preprocess, 'api/cosim/preprocess')

if __name__ == "__main__":
    app.run(debug=True)