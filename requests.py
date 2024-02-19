import requests

import json

url = 'http://127.0.0.1:5000'

response = requests.post(url)


json_text = json.loads(response.text)

print(json_text)
