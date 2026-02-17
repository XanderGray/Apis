import requests, time


while True:
    api = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(api)
    print(response.json()["message"])
    time.sleep(10)


