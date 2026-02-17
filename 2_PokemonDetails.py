import requests

while True:
    pokemon = str(input("Enter the name of your pokemon: ")).lower()
    api = "https://pokeapi.co/api/v2/pokemon/" + pokemon.lower()
    response = requests.get(api)

    abilitydesc = input("Do you want to see the abilities of your pokemon? (yes/no): ").lower()
    if abilitydesc == "yes":
        abilities = response.json()["abilities"]
        for ability in abilities:
            print(ability["ability"]["name"])

    moveset = input("Do you want to see the moves of your pokemon? (yes/no): ").lower()
    if moveset == "yes":
        moves = response.json()["moves"]
        for move in moves:
            print(move["move"]["name"])

    types = input("Do you want to see the types of your pokemon? (yes/no): ").lower()
    if types == "yes":
        type = response.json()["types"]
        for t in type:
            print(t["type"]["name"])

    basestats = input("Do you want to see the stats of your pokemon? (yes/no): ").lower()
    if basestats == "yes":
        stats = response.json()["stats"]
        for stat in stats:
            print(stat["stat"]["name"] + ": " + str(stat["base_stat"]))