import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("sikretong_key", "dev")
    HF_API_KEY = os.getenv("api_secret_key")