"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from emotionDetection import emotion_detection as em

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    """
    Handles emotion detection requests.

    Returns:
        str: A formatted response with emotion analysis or an error message.
    """
    # Get the 'textToAnalyze' query parameter
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    print(f"Received text: '{text_to_analyze}'")  # Debugging statement

    # Call the emotion detection function
    emotion_data = em.emotion_detector(text_to_analyze)
    print(f"Emotion Data: {emotion_data}")  # Debugging statement

    if emotion_data['dominant_emotion'] is None:
        return "Invalid Text, please try again!"

    return f"""
        For the given statement, the system response is:
        - Anger: {emotion_data['anger']}
        - Disgust: {emotion_data['disgust']}
        - Fear: {emotion_data['fear']}
        - Joy: {emotion_data['joy']}
        - Sadness: {emotion_data['sadness']}
        The dominant emotion is: {emotion_data['dominant_emotion']}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
