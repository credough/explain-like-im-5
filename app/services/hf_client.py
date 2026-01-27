import requests
from flask import current_app
from ..utils.text_levels import LEVEL_PROMPTS

HF_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

def simplify_text(text, level):
    prompt = LEVEL_PROMPTS.get(level, LEVEL_PROMPTS["eli5"])


    payload = {
       "inputs": f"{prompt}: {text}"
    }


    headers = {
       "Authorization": f"Bearer {current_app.config['HF_API_KEY']}"
    }


    response = requests.post(HF_URL, headers=headers, json=payload)


    if response.status_code != 200:
      return "Error generating explanation"


    return response.json()[0]["generated_text"]