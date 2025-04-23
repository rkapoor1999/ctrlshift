import argparse
import time
from pytrends.request import TrendReq


def fetch_trends(keywords):
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Google Trends data for given keywords.")
    parser.add_argument("keywords", nargs="+", help="Keyword(s) to fetch trends for")
    args = parser.parse_args()

    trends_data = fetch_trends(args.keywords)

    if trends_data.empty:
        print("No data found.")
    else:
        print(trends_data)
