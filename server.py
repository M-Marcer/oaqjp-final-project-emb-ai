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
    emotion_result = EM.emotion_detector(text_to_analyze)
    print(emotion_result)
    return emotion_result

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)