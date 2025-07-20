🛡️ Phishing URL Detector
A machine learning-powered web application that detects phishing URLs using advanced feature extraction and a Random Forest classifier.
---
🚀 Features
🔎 Real-time URL Analysis: Instantly classify URLs as phishing or legitimate
---
🧠 Advanced Feature Extraction: Analyzes 25+ characteristics, including:

URL length and structure

Domain traits and TLDs

Special character patterns

Suspicious keywords and file types

IP address usage and shorteners

🌲 Machine Learning Model: Trained Random Forest Classifier

🖥️ Web Interface: Simple and responsive Flask-based UI

📊 Confidence Scoring: Outputs probability and risk levels (SAFE, LOW, MEDIUM, HIGH)

🚀 Deployment Ready: Optimized for cloud platforms like Render
---
🏗️ Project Structure
bash
Copy
Edit
phishing-url-detector/
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── train_model.py          # Model training script
├── phishing_model.pkl      # Trained model
├── utils/
│   ├── __init__.py
│   └── url_features.py     # Feature extraction functions
├── templates/
│   └── index.html          # UI template
├── data/
│   └── sample_urls.csv     # Sample dataset
└── README.md
---
🛠️ Installation & Setup
📍 Local Development
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python train_model.py          # Train the model
python app.py                  # Run the app
Access the app at http://localhost:5000
---
🌐 Deploy on Render
Push your code to a GitHub repository

Go to https://render.com

Create a New Web Service

Connect your GitHub repo

Configure deployment:

Build Command:
pip install -r requirements.txt && python train_model.py

Start Command:
python app.py

Environment:
Python 3
---
🧠 Machine Learning Model
Algorithm: Random Forest Classifier

Features Extracted (25):

URL length, domain length, path length

Dot, slash, hyphen, digit, special char counts

IP address detection, HTTPS check

Suspicious TLDs, subdomains, and keywords

Shortener detection and domain flags

Accuracy: ~95% on test data

Validation: Stratified train-test split
---
🔧 API Endpoints
POST /predict

{
  "url": "https://example.com"
}
Response:

{
  "url": "https://example.com",
  "prediction": "legitimate",
  "confidence": 0.95,
  "risk_level": "SAFE",
  "features": {...}
}
POST /batch_predict
json
Copy
Edit
{
  "urls": ["https://site1.com", "http://phishing-link.com"]
}
GET /model_info
{
  "accuracy": 0.95,
  "feature_count": 25,
  "model_type": "Random Forest"
}
GET /health
Returns: {"status": "healthy"}
---

📊 Model Training
Retrain the model on your own dataset:

python train_model.py
Make sure your CSV includes labeled URLs (0 for legit, 1 for phishing).

🚨 Important Notes
This is a demo tool for educational use

The model checks URL structure only

Not a substitute for full threat detection

Always validate URLs using external threat feeds or reputation APIs in production

🤝 Contributing
Fork this repo

Create a feature branch

Add tests where needed

Submit a pull request

📝 License
This project is for academic and educational use. Please verify third-party library licenses before using commercially.
