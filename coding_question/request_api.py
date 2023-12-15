import requests
import json

api_key = 'e55e5f5c3169175f86e872b335f33dab'
apiURL = f'https://api.openweathermap.org/data/2.5/weather?q=Vancouver&appid={api_key}'

response = requests.get(apiURL)
# print(type(response.json()))
# json_response = json.loads(response.text)
# print(type(json_response))
# print(json_response['weather'])

json_response = response.json()
print(json_response)
print(type(json_response))
print(json_response['weather'][0]['description'])
