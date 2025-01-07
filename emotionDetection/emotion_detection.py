import requests
import json

def emotion_detector(text_to_analyze):
    
    # Define the API endpoint and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Construct the payload
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=header)
    print(f"Response Status Code: {response.status_code}")  # Debugging output

    # Handle the response based on status code
    if response.status_code == 200:
        # Parse the JSON response
        formatted_response = json.loads(response.text)
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        # Determine the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Construct the output dictionary
        output = {
            **emotion_scores,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # Handle blank or invalid input by returning None values
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        print("Error: The input text is blank or invalid.")

    return output
