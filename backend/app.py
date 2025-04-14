from flask import Flask, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS  # <-- Import flask_cors

app = Flask(__name__)

# Enable CORS for all origins
CORS(app)  # This enables CORS for all routes

# Optionally, to allow only specific origins (e.g., frontend running on localhost:3000)
# CORS(app, origins=["http://localhost:3000"])

# Connect to local MongoDB
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/DockerTest")
client = MongoClient(MONGO_URI)
db = client.get_database()

@app.route('/')
def home():
    # Example: count documents
    count = db.test.count_documents({})
    return jsonify(message="Connected to Local MongoDB", docs=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
