from pytrends.request import TrendReq
import time


def fetch_trends():
    # The user must manually edit this keyword!
    keywords = ["nike dunks"]  # <--- Change this manually
    
    # Initialize pytrends and set the timeframe to 1 year
    pytrends = TrendReq(hl='en-US', tz=360)

    # Add a delay to prevent hitting Google's rate limits
    time.sleep(5)  # Adjust this if necessary
    pytrends.build_payload(keywords, timeframe='today 12-m')  # Past 1 year

    # Fetch the interest over time data
    data = pytrends.interest_over_time()

    if not data.empty:
        data = data.drop(columns=['isPartial'])

    return data


# Example usage
if __name__ == "__main__":
    trends_data = fetch_trends()

    if trends_data.empty:
        print("No data found.")
    else:
        print(trends_data)
