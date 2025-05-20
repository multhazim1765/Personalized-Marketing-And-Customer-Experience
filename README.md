# Personalized Marketing and Customer Experience

## 🎯 Objective
To build an intelligent web-based system that provides personalized product recommendations, analyzes customer feedback, and simulates IoT-driven environment data to enhance the customer experience.

---

## 🚀 Features

- 🤖 **Product Chatbot** – Suggests offers based on product interest
- 💬 **Sentiment Analysis** – Analyzes customer feedback in real-time
- 👥 **User Recommendation System** – Finds similar users using Nearest Neighbors
- 🌡️ **IoT Data Simulation** – Displays simulated temperature, humidity, and foot traffic data
- 📊 **Dashboard Interface** – Simple HTML/JS frontend for interacting with all features

---

## 🛠️ Technologies Used

- **Python**
- **Flask** – Web framework
- **Scikit-learn** – ML model training
- **TextBlob** – Sentiment analysis
- **pandas & NumPy** – Data manipulation
- **NearestNeighbors (Sklearn)** – User similarity
- **HTML + JavaScript** – Frontend interface

---

## ⚙️ How It Works

1. **Homepage:** Offers an interactive dashboard.
2. **Chatbot:** User enters a product name → receives a tailored message.
3. **Sentiment Analysis:** User submits feedback → TextBlob classifies it as positive, neutral, or negative.
4. **Recommendations:** Predefined vector input → finds similar users using cosine similarity.
5. **IoT Simulation:** `/environment` API returns dynamic sensor-like data.

---

## 📦 Installation

### ✅ Option 1: In Jupyter Notebook

Paste the following into a notebook cell to install all required packages:

```python
!pip install flask numpy pandas scikit-learn textblob
!python -m textblob.download_corpora
```

---

### ✅ Option 2: In Terminal

Run this in your system terminal (Command Prompt, Bash, etc.):

```bash
pip install flask numpy pandas scikit-learn textblob
python -m textblob.download_corpora
```

---

These dependencies are needed for:

* `Flask`: Web app and API routing
* `NumPy`, `Pandas`: Data handling
* `scikit-learn`: Machine learning models
* `TextBlob`: Sentiment analysis
