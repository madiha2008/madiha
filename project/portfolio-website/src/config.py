from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_default_secret_key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///c:/Users/vmaah/OneDrive/Desktop/madiha_project/protofolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False