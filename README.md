# 🏏 Cricket Play Predictor

A Machine Learning powered web application that predicts **whether the current weather conditions are suitable for playing cricket** using **live weather data** and a **Gaussian Naive Bayes classification model**.

The application takes a **city name** as input, fetches the latest weather information from the **OpenWeatherMap API**, preprocesses the data, and predicts whether it is a good day to play cricket.

---

## 🚀 Live Demo

https://cricket-play-predictor-lyyf.onrender.com

---

## 📸 Preview

### Home Page
- Enter any city name.
- Fetches live weather information.
- Predicts whether cricket can be played.

### Result Page
Displays:

- 📍 City Name
- 🌦 Weather Condition
- 🌡 Temperature
- 💧 Humidity
- 🌬 Wind Speed
- 🏏 Cricket Play Prediction

---

# ✨ Features

- 🌍 Predicts using **live weather data**
- 🤖 Machine Learning based prediction
- 🏏 Determines whether cricket can be played
- ⚡ Fast Flask backend
- 🎨 Responsive and modern UI
- 🚫 Handles invalid city names gracefully
- 📊 Uses trained Gaussian Naive Bayes model

---

# 🧠 Machine Learning Model

Algorithm Used:

- **Gaussian Naive Bayes**

The model is trained using weather-related features including:

- Temperature
- Humidity
- Wind Speed
- Weather Condition

The categorical weather conditions are encoded before training and used during prediction.

---

# 🛠 Tech Stack

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- Gaussian Naive Bayes
- Joblib

### Frontend

- HTML5
- CSS3

### API

- OpenWeatherMap API

---

# 📂 Project Structure

```text
cricket_play_predictor/
│
├── app.py
├── model.pkl
├── labelencode.pkl
├── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── result.html
│   └── result2.html
│
├── static/
│   ├── home.css
│   └── result.css
│
└── indian_cricket_weather_dataset_100000.csv
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cricket_play_predictor.git
```

Move into the project directory:

```bash
cd cricket_play_predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

# 🔑 OpenWeatherMap API Setup

Create a free API key from:

https://openweathermap.org/api

Replace:

```python
api_key = "YOUR_API_KEY"
```

or preferably configure it as an environment variable before deployment.

---

# 📊 Prediction Workflow

```text
User enters city
        │
        ▼
Flask Application
        │
        ▼
OpenWeatherMap API
        │
        ▼
Current Weather Data
        │
        ▼
Feature Extraction
        │
        ▼
Gaussian Naive Bayes Model
        │
        ▼
Prediction
        │
        ▼
Can Play Cricket?
        Yes / No
```

---

# 📦 Python Libraries Used

- Flask
- Requests
- Joblib
- NumPy
- Pandas
- Scikit-learn
- SciPy
- Gunicorn

---

# 🎯 Future Improvements

- 🌧 Include rainfall and cloud cover as additional features
- 📈 Improve model accuracy using Random Forest or XGBoost
- 📍 Add location autocomplete
- 📊 Display probability/confidence score
- 📱 Mobile-friendly enhancements
- 🌐 Deploy on Render with environment variables

---

# 👨‍💻 Author

**Harsha Paloju**

Aspiring AI Engineer passionate about Machine Learning, Flask, and building real-world AI applications.

If you like this project, don't forget to ⭐ star the repository!
