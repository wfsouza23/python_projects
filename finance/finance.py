import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_ID = os.getenv('API_ID_FINANCE')

url = "https://rapidapi.p.rapidapi.com/market/get-price-chart"

querystring = {"id":"inmex:ind","interval":"y1"}

headers = {
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com",
    'x-rapidapi-key': API_ID
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)