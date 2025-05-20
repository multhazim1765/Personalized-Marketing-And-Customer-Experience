# Import necessary libraries
import time, random, numpy as np, pandas as pd
from flask import Flask, request, jsonify, render_template_string
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import NearestNeighbors
from textblob import TextBlob
import threading

# Initialize Flask web application
app = Flask(__name__)

# Generate dummy customer data
def generate_customer_data(n=100):
    # Randomly generate 3 features (e.g., age, income, score)
    X = np.random.randint(18, 65, size=(n, 3))
    # Label customers based on the 3rd feature value
    y = (X[:, 2] > 50).astype(int)
    return X, y

# Simulate IoT data such as temperature and humidity
def simulate_iot_data_stream():
    return {
        "temperature": round(random.uniform(20.0, 25.0), 2),
        "foot_traffic": random.randint(50, 200),
        "humidity": round(random.uniform(30.0, 50.0), 2),
    }

# Train a simple ML model using RandomForest
def train_model():
    X, y = generate_customer_data(500)
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

# Simple chatbot response generator based on product input
def chatbot_response(product):
    return f"Hey! Because you're interested in {product}, here's a custom deal just for you!"

# Static customer features for similarity recommendation
customer_data = {
    'user_id': [1, 2, 3, 4, 5],
    'feature_1': [0.1, 0.2, 0.2, 0.4, 0.9],
    'feature_2': [0.3, 0.6, 0.7, 0.1, 0.8],
    'feature_3': [0.4, 0.8, 0.5, 0.2, 0.3]
}
df = pd.DataFrame(customer_data)

# Fit the Nearest Neighbors model for recommendations
recommender = NearestNeighbors(metric='cosine', algorithm='brute')
recommender.fit(df.drop(['user_id'], axis=1))

# Store user feedback and sentiment results
feedback_log = []

# Define the homepage of the app with HTML and JavaScript
@app.route("/")
def dashboard():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head><title>Marketing System</title></head>
    <body>
        <h1>Personalized Marketing Dashboard</h1>

        <h3>Try Product Chatbot</h3>
        <input id="prod" placeholder="Product name" />
        <button onclick="askBot()">Ask</button>
        <p id="botRes"></p>

        <h3>Analyze Feedback</h3>
        <input id="textInput" placeholder="Your feedback" />
        <button onclick="analyze()">Check</button>
        <p id="sentimentRes"></p>

        <h3>Get Similar Users</h3>
        <button onclick="recommend()">Recommend</button>
        <p id="recs"></p>

        <script>
            function askBot() {
                let val = document.getElementById("prod").value;
                fetch("/chatbot", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ product: val })
                }).then(r => r.json()).then(d => {
                    document.getElementById("botRes").innerText = d.response;
                });
            }

            function analyze() {
                let text = document.getElementById("textInput").value;
                fetch("/sentiment", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ text: text })
                }).then(r => r.json()).then(d => {
                    document.getElementById("sentimentRes").innerText = "Sentiment: " + d.sentiment;
                });
            }

            function recommend() {
                fetch("/recommend", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ vector: [0.2, 0.5, 0.8] })
                }).then(r => r.json()).then(d => {
                    document.getElementById("recs").innerText = "Similar users: " + d.recommendations.join(", ");
                });
            }
        </script>
    </body>
    </html>
    """)

# Route to handle chatbot product recommendations
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    reply = chatbot_response(data["product"])
    return jsonify({"response": reply})

# Route to handle feedback sentiment analysis
@app.route("/sentiment", methods=["POST"])
def sentiment():
    text = request.json["text"]
    polarity = TextBlob(text).sentiment.polarity
    sentiment = "positive" if polarity > 0.1 else "negative" if polarity < -0.1 else "neutral"
    feedback_log.append({"text": text, "sentiment": sentiment})
    return jsonify({"sentiment": sentiment})

# Route to find similar users using vector-based recommendation
@app.route("/recommend", methods=["POST"])
def recommend():
    vector = request.json["vector"]
    d, i = recommender.kneighbors([vector], n_neighbors=3)
    recs = df.iloc[i[0]]['user_id'].tolist()
    return jsonify({"recommendations": recs})

# Route to show simulated environment sensor data
@app.route("/environment")
def environment():
    return jsonify(simulate_iot_data_stream())

# Start Flask app in a new thread
def run_app():
    app.run(port=5000, debug=False, use_reloader=False)

# Start the server
thread = threading.Thread(target=run_app)
thread.start()
