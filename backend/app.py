from trend_data import fetch_trends  # Ensure trend_data.py is in the same directory
from flask import Flask, jsonify

app = Flask(__name__)

# Route to fetch Google Trends data
@app.route('/api/google-trends', methods=['GET'])
def google_trends():
    trends_data = fetch_trends()  # No more keyword input!

    if trends_data is not None and not trends_data.empty:
        trends_data.index = trends_data.index.strftime('%Y-%m-%d')  # Format the timestamps
        return jsonify(trends_data.to_dict())
    else:
        return jsonify({"error": "No trends data found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
