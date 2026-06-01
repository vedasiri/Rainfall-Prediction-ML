# 🌧️ Rainfall Prediction AI

A Machine Learning-based web application that predicts whether rainfall is expected based on weather conditions. The project uses a Random Forest Classifier with hyperparameter tuning and provides both single prediction and batch CSV prediction through an interactive Streamlit interface.

---

## LIVE DEMO
https://rainfall-prediction-ai.streamlit.app/


# 🚀 Features

* 🌧️ Rainfall / No Rainfall Prediction
* 🤖 Random Forest Machine Learning Model
* ⚙️ Hyperparameter Tuning using GridSearchCV
* 📊 Feature Importance Analysis
* 🎯 Prediction Confidence Score
* 📂 Batch Prediction using CSV Upload
* ⬇️ Download Prediction Results
* 🎨 Modern Streamlit User Interface
* 💾 Saved Model using Joblib

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Streamlit
* Joblib

streamlit (web app)
Pandas (data handling)
NumPy (arrays)
Scikit-Learn (ML model)
Matplotlib (feature importance plots)
Joblib (save/load model)
Imbalanced-Learn (SMOTE/downsampling support)


---

# 📁 Project Structure

```text
Rainfall-Prediction-ML/
│
├── app.py
├── rainfall_model.pkl
├── Rainfall.csv
├── test_data.csv
├── README.md
├── requirements.txt
├── .gitignore
└── Rainfall_Prediction_using_Machine_Learning.ipynb
```

---

# 📊 Dataset Features

The model predicts rainfall using:

* Pressure
* Dew Point
* Humidity
* Cloud Cover
* Sunshine Hours
* Wind Direction
* Wind Speed

Target Variable:

* Rainfall

  * 0 = No Rainfall
  * 1 = Rainfall

---

# 🧠 Machine Learning Workflow

1. Data Preprocessing
2. Class Balancing
3. Train-Test Split
4. Random Forest Training
5. Hyperparameter Tuning using GridSearchCV
6. Model Evaluation
7. Feature Importance Analysis
8. Model Saving
9. Streamlit Application Development

---

# 📈 Model Performance

### Random Forest Classifier

* Cross Validation Accuracy: 81.9%
* Test Accuracy: 74.5%

### Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

# 📌 Feature Importance

| Feature        | Importance |
| -------------- | ---------- |
| Cloud          | 25.7%      |
| Sunshine       | 24.5%      |
| Humidity       | 15.5%      |
| Wind Speed     | 11.8%      |
| Dew Point      | 11.2%      |
| Pressure       | 7.8%       |
| Wind Direction | 3.6%       |

---

# 📂 Batch Prediction

Upload a CSV file containing:

```csv
pressure,dewpoint,humidity,cloud,sunshine,winddirection,windspeed
990,25,95,90,1,180,25
1020,10,30,10,10,180,5
1008,18,60,40,6,120,12
```

The application predicts rainfall for all rows and allows downloading the results.

---

# ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

# 👨‍💻 Author

Veda  Sri Kalla

B.Tech Mechanical Engineering Student at IIT DHANBAD

Machine Learning & AI Enthusiast

---

# ⭐ Project Highlights

* End-to-End Machine Learning Project
* Model Training & Evaluation
* Hyperparameter Optimization
* Interactive Web Application
* CSV Batch Prediction Support
* GitHub Portfolio Ready
