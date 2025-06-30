# 📰 Fake News Detector

## 🔍 Description
This project is a Flask web application that allows users to input a news article and determine whether it is real or fake using a machine learning model.

## 🛠 Technologies
- Python
- Scikit-learn
- Flask
- TfidfVectorizer
- PassiveAggressiveClassifier
- HTML

## 🧪 How to Run

1. **Install requirements**  
```bash
pip install flask scikit-learn pandas
```

2. **Prepare your dataset**  
Place a CSV file named `news.csv` in the root folder with two columns: `text` and `label`.

3. **Train the model**  
```bash
python train_model.py
```

4. **Run the app**  
```bash
python app.py
```

5. Open browser and visit:  
`http://127.0.0.1:5000/`

## 📁 Files
- `app.py` → Flask app
- `train_model.py` → Model training script
- `model.pkl` and `vectorizer.pkl` → Saved model and vectorizer
- `templates/index.html` → Web UI

## 👨‍💻 Author
sekhar371 | saisekhar179@gmail.com