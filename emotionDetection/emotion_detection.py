import requests
import json

def emotion_detector(text_to_analyze):
    
    # Test case to work offline
    env_type = "test"

    if env_type == "test":
        output = {
            'anger': 0.1,
            'disgust': 0.1,
            'fear': 0.1,
            'joy': 0.1,
            'sadness': 1,
            'dominant_emotion': 'sadness'
            }
        
    else: 

        url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        myobj = { "raw_document": { "text": text_to_analyze } }
        response = requests.post(url, json = myobj, headers=header) 
        formatted_reposnse = json.loads(response.text)

        if response.status_code == 200: 
       # Extract emotion predictions
            emotion_scores = formatted_reposnse['emotionPredictions'][0]['emotion']

            # Determine the dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Create the output dictionary
            output = {
                **emotion_scores,
                'dominant_emotion': dominant_emotion
            }

        elif response.status_code == 400:            
            output = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None,
            }
            
    return output  # Return the result
