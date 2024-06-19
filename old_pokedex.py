'''
    pip install Pillow
    pip install requests
    pip install pydub
'''
import requests
from PIL import Image
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def main():
    print("Please enter the name or ID of the Pokémon you would like to search for:")
    while True:
        pokemon_name = input().replace(" ", "-").lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        if response.status_code == 200:
            break
        else:
            print("I could not find that Pokémon, please try again.")
            
    pokemon = response.json()
    print_pokemon(pokemon)
    
    if input("Would you like to search for another Pokémon? (y/n)").lower() == 'y':
        main()
    else:
        print("We hope to see you again!")

def rgb_to_ansi(r, g, b):
    return f"\033[48;2;{r};{g};{b}m  \033[0m"

def print_pokemon(pokemon):
    url = pokemon['sprites']['front_default']
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content)).convert('RGBA')
        img = img.crop((5, 5, 90, 90)).resize((40, 40))
        
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = img.getpixel((x, y))
                if a > 0:
                    print(rgb_to_ansi(r, g, b), end='')
                else:
                    print('  ', end='')

            if y == 30:
                print(f"Name: {pokemon['name']}")
            elif y == 31:
                print(f"ID: {pokemon['id']}")
            elif y == 32:
                print(f"Height: {pokemon['height']}")
            elif y == 33:
                print(f"Weight: {pokemon['weight']}")
            elif y == 34:
                type_names = [t['type']['name'] for t in pokemon['types']]
                print(f"Types: {', '.join(type_names)}")
            else:
                print('')

if __name__ == "__main__":
    print("Hello, welcome to the Pokedex!")
    main()
