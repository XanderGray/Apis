import requests, time

while True:
    api = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api)
    print(response.json()["value"])
    time.sleep(10)