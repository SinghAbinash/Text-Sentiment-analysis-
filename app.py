from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    blob = TextBlob(text)
    
    #1 ovr-score
    overall_score = blob.sentiment.polarity
    if overall_score > 0:
        label = "Positive"
    elif overall_score < 0:
        label = "Negative"
    else:
        label = "Neutral"

    words_analysis = []
    for word in blob.words:
        # We must create a new TextBlob for the individual word to get its specific score
        word_blob = TextBlob(word)
        w_score = word_blob.sentiment.polarity
        
        w_label = "Neutral"
        if w_score > 0: w_label = "Positive"
        if w_score < 0: w_label = "Negative"
        
        words_analysis.append({
            "word": word,
            "score": w_score,
            "label": w_label
        })
    
    return jsonify({
        "overall_label": label,
        "overall_score": overall_score,
        "words": words_analysis
    })

if __name__ == '__main__':
    app.run(debug=True)