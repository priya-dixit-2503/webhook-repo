from flask import Blueprint, request, jsonify
from datetime import datetime
from pymongo import MongoClient
import os

webhook = Blueprint('webhook', __name__)

client = MongoClient(os.getenv('MONGO_URI'))
db = client['github_events']
collection = db['events']

@webhook.route('/webhook', methods=['POST'])
def receive_webhook():
    # your logic here
    return jsonify({"status": "ok"}), 200
