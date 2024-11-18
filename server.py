''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and runs emotion detection over it
        using emotion_detector() function. The output returned shows the dominant emotion
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_sc = response['anger']
    disgust_sc = response['disgust']
    fear_sc = response['fear']
    joy_sc = response['joy']
    sadness_sc = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    return_stmt = "For the given statement, the system response is 'anger': {}, 'disgust': "
    return_stmt += "{}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}."
    return  return_stmt.format(anger_sc, disgust_sc, fear_sc, joy_sc, sadness_sc, dominant_emotion)

@app.route("/")
def render_index_page():
    '''  This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
