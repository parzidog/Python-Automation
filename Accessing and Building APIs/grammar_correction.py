import requests
import json

# Use the Language Tool API

url = "https://api/languagetool.org/v2/check"
text = "I ain't no fool!"
data = {"text": text, "language": "auto"}

response = requests.post(url, data=data)

result = json.loads(response.text)
