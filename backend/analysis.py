# app.py
from flask import Flask, jsonify, request
from trend_data import fetch_google_trends
from analysis import calculate_popularity_change
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Fashion Trend Predictor API"})

@app.route('/api/popularity-change', methods=['POST'])
def popularity_change():
    data = request.json
    old_data = pd.Series(data['old_data'])
    new_data = pd.Series(data['new_data'])
    changes = calculate_popularity_change(new_data, old_data)
    return jsonify(changes.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
