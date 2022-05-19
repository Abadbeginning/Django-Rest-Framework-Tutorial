import requests

entpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)
print("text ==>", get_response.text)

# HTTP Request -> HTML
# REST API HTTP Request
print("json ==>", get_response.json())
