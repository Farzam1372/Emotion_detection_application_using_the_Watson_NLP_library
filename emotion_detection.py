import requests
import json

#Creating a package
def emotion_detector(text_to_analyse):
    
    #End point and header
    URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #Input jason
    Input_jsonnput_json: { "raw_document": { "text": text_to_analyse } }

    #Send post request
    response = request.post(URL, Headers=Headers, json=Input_json)

    #Return the text
    return response.text

