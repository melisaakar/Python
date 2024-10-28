import requests


def get_pokemon_info(pokemon_name):
    # PokeAPI URL'si
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/"

    # API isteğini gönder
    response = requests.get(url)

    # Yanıtı kontrol et
    if response.status_code == 200:
        data = response.json()

        # Pokémon bilgilerini çıkar
        name = data['name']
        height = data['height']
        weight = data['weight']
        types = [t['type']['name'] for t in data['types']]

        # Bilgileri yazdır
        print(f"Pokémon: {name.capitalize()}")
        print(f"Yükseklik: {height}")
        print(f"Ağırlık: {weight}")
        print(f"Türler: {', '.join(types)}")
    else:
        print("Pokémon bulunamadı.")


# Kullanıcıdan Pokémon adı al
pokemon_name = input("Pokémon adını girin: ")
get_pokemon_info(pokemon_name)
