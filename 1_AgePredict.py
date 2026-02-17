import requests

while True:
    name = str(input("Enter the your name to see your real age: ")).title()
    api = "https://api.agify.io?name=" + name
    response = requests.get(api)
    print(f"{name} is {response.json()['age']} years old")