from flask import Flask, render_template, request
import joblib
from utils.url_features import extract_features
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)[0]
    result = "Phishing ⚠️" if prediction == 1 else "Legitimate ✅"
    return render_template('index.html', prediction=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
