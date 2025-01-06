let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let emotionData = JSON.parse(this.responseText);
            console.log(emotionData);
            let ouptutHTML = `
                <p> For the given statement, the system response is 
                'anger': ${emotionData.anger},
                'disgust': ${emotionData.disgust},
                'fear': ${emotionData.fear},
                'joy': ${emotionData.joy} and
                'sadness': ${emotionData.sadness}.
                The dominant emotion is ${emotionData.dominant_emotion}.
                </p>
                `;

            document.getElementById("emotion-result").innerHTML = ouptutHTML;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}
