import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_fashion_data():
    # Replace this URL with the URL of the fashion website you want to scrape
    url = 'https://www.vogue.com/fashion'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example data extraction - modify the selectors to fit the website's structure
        data = []
        for item in soup.select('.garment-item'):
            name = item.select_one('.garment-name').get_text(strip=True)
            popularity = item.select_one('.popularity-score').get_text(strip=True)
            data.append({'name': name, 'popularity': float(popularity)})
        
        # Convert data to a DataFrame and return it as a dictionary
        df = pd.DataFrame(data)
        return df.to_dict(orient='records')
    else:
        print("Failed to retrieve data")
        return None
