# train_model.py - Trains the fake news detection model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle

# Load dataset
df = pd.read_csv("news.csv")  # Should contain 'text' and 'label' columns

# Split data
x_train, x_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

# Train model
model = PassiveAggressiveClassifier()
model.fit(x_train_vec, y_train)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# Evaluate
score = model.score(x_test_vec, y_test)
print(f"Model Accuracy: {score:.2f}")