# app/__init__.py
from flask import Flask
from app.webhook.routes import webhook  # ✅ Correct import

def create_app():
    app = Flask(__name__)
    app.register_blueprint(webhook)
    return app
