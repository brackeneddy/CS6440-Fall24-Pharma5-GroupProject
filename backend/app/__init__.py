from flask import Flask
from flask_cors import CORS

def create_app():
    application = Flask(__name__)
    
    CORS(application)

    from app.routes import main
    application.register_blueprint(main, url_prefix="/")

    return application
