import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from utils.url_features import extract_features_from_dataframe

# Load dataset
df = pd.read_csv('data/phishing_url_dataset.csv')

# Extract features
X = extract_features_from_dataframe(df['URL'])
y = df['Label']

# Train and evaluate 10 times
print("Training and evaluating model 10 times:\n")
best_accuracy = 0
best_model = None

for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Run {i+1}: Accuracy = {acc * 100:.2f}%")
    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model

# Save best model
if best_model:
    joblib.dump(best_model, 'model.pkl')
    print(f"\nBest model saved with accuracy: {best_accuracy * 100:.2f}%")

