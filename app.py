import requests
import json
import uvicorn
from config import secret_key, zone

from fastapi import FastAPI
app = FastAPI()

headers = { "Content-Type":"application/json",
                       "Ocp-Apim-Subscription-Key":secret_key,
                       "Ocp-Apim-Subscription-Region":zone
                       
                   }

@app.get("/get_all")
def get_all_languages():
    print("here")
    data = requests.get('https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=translation')
    return data.json()

@app.post("/translate_text/")
def translate_text(lang, text):
    """
    input params type {'text':"", "lang":""}
    """
    data =requests.post("https://api.cognitive.microsofttranslator.com/translate?",
                    json=[{"Text":text}],
                    params={"api-version":"3.0","to":lang},
                    headers=headers)
    return data.json()[0]['translations']

@app.post("/detect_language/")
def detect_text(text):
    """
    input params type {'text':""}
    """
    data =requests.post("https://api.cognitive.microsofttranslator.com/detect?",
                    json=[{"Text":text}],
                    params={"api-version":"3.0"},
                    headers=headers)
    return data.json()

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='68.183.31.221')