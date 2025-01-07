from flask import Flask, render_template, request, jsonify
from emotionDetection import emotion_detection as EM

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    # Get the 'textToAnalyze' query parameter
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    # Call the emotion detection function
    emotionData = EM.emotion_detector(text_to_analyze)
    print(emotionData)

    if emotionData['dominant_emotion'] is None:
        return "Invalid Text, please try again!"
    else:
        out_message = f"""
            For the given statement, the system response is:
            - Anger: {emotionData['anger']}
            - Disgust: {emotionData['disgust']}
            - Fear: {emotionData['fear']}
            - Joy: {emotionData['joy']}
            - Sadness: {emotionData['sadness']}
            The dominant emotion is: {emotionData['dominant_emotion']}
            """
        print(out_message)
        return out_message

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)