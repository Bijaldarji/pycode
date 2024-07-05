# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Example word lists based on stylistic or thematic differences
male_words = ["sports", "car", "technology", "work", "money", "football", "tools"]
female_words = ["fashion", "shopping", "beauty", "love", "family", "recipe", "cute"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data['text']
    text_words = text.lower().split()
    
    male_score = sum(word in text_words for word in male_words)
    female_score = sum(word in text_words for word in female_words)
    
    if male_score > female_score:
        prediction = "Male"
    elif female_score > male_score:
        prediction = "Female"
    else:
        prediction = "Unknown"

    return jsonify({'prediction': prediction, 'trained': True})

if __name__ == '__main__':
    app.run(debug=True)
