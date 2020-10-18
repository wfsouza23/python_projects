import requests

url = "https://rapidapi.p.rapidapi.com/market/get-price-chart"

querystring = {"id":"inmex:ind","interval":"y1"}

headers = {
    'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com",
    'x-rapidapi-key': "b4432960abmshb29b38f838286fdp12a6b3jsn07b906ad65c3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)