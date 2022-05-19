import requests

entpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint)
print("text ==>", get_response.text)

# HTTP Request -> HTML
# REST API HTTP Request
print("json ==>", get_response.json())
