import requests

key = "f1afac82739e42d595f39ebe90692b10"
url = f"http://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-5-27&to=2023-5-28&sortBy=popularity&language=en&apiKey={key}"

r = requests.get(url)

content = r.json()
print(content["articles"][0]["title"])
