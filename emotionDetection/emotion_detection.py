import requests
import json

def emotion_detector(text_to_analyze):
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
        
        anger_score = formatted_reposnse['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_reposnse['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_reposnse['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_reposnse['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_reposnse['emotionPredictions'][0]['emotion']['sadness']

        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # Determine the dominant emotion with max function
        dominant_emotion = max(emotions, key=emotions.get)

        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }

    return output  # Return the result

    # return formatted_reposnse['emotionPredictions'][0]['emotion']

# text_to_analyze = "Ever since I saw the movie Gladiator, I have been dreaming of visiting the Colosseum in Rome. I opened the Google Arts App, and there I was, standing on the street overlooking the Colosseum. At first sight, its huge immensity took my breath away. It was once an arena that housed bloodthirsty Romans as they watched gladiators tear each other apart. I walked through the trenches built for the Gladiators. Row after row of humble houses constructed out of grey rock were overshadowed by the huge seating stands above them. The stands themselves were stacked on top of each other. I imagined crowds of Romans screaming and cheering for their champions. As I entered the amphitheatre, the first thing that I noticed was the renovation. I was distracted by the shiny steel beams that contrasted with the old rock. In the heart of the arena lies the sand pit where the bloodsport took place. I climbed on top of the high overwatch from where the royalty watched the carnage. Watching from above, I noticed the pits inside the arena, from which caged wild animals must have been unleashed. Then I climbed below and entered the cells from which the Gladiators must have made their entry. Standing in this entryway made me realise that I cannot judge the Romans for enjoying the bloodsport. We modern humans today are drawn to the same violence in action films. We still flock together to watch MMA and boxing matches. This revelation burned deep within my heart as I ended my virtual tour."
# print(emotion_detector(text_to_analyze))