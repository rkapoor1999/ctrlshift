from sklearn.linear_model import LinearRegression
import pandas as pd

# Example function to analyze and predict trend popularity
def predict_trends(data):
    df = pd.DataFrame(data)
    
    # Assuming 'time' and 'popularity' columns exist in the data
    X = df[['time']]  # Extracting the 'time' feature
    y = df['popularity']
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Define the next time period
    next_time = X.iloc[-1, 0] + 1  # This assumes 'time' is an integer sequence
    
    # Predict trend popularity increase/decrease
    prediction = model.predict([[next_time]])
    percentage_change = (prediction[0] - y.iloc[-1]) / y.iloc[-1] * 100
    return percentage_change
