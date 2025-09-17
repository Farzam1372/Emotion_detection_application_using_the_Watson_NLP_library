import requests
import json

#creating a package
def emotion_detector(text_to_analyse):
    
    #end point and header
    URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #input jason
    Input_jsonnput_json: { "raw_document": { "text": text_to_analyse } }

    #send post request
    response = request.post(URL, Headers=Headers, json=Input_json)

    #return the text
    return response.text

