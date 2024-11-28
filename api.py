import random
from io import BytesIO

import requests
from PIL import Image, ImageTk


# Function to fetch a random Pokémon from PokéAPI
def get_random_pokemon():
    pokemon_id = random.randint(1, 151)  # Get a random Pokémon from the first 151 (Gen 1)
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    data = response.json()
    
    # Fetch necessary Pokémon data
    pokemon_name = data['name'].capitalize()
    pokemon_sprite_url = data['sprites']['front_default']
    
    # Get sprite image from URL
    sprite_response = requests.get(pokemon_sprite_url)
    sprite_img = Image.open(BytesIO(sprite_response.content)).resize((160, 160))
    sprite = ImageTk.PhotoImage(sprite_img)
    
    # Fetch Pokémon types (assuming the first type is the primary type)
    pokemon_types = [type_info['type']['name'].capitalize() for type_info in data['types']]
    primary_type = pokemon_types[0] if pokemon_types else "Unknown"

    return {
        'id': pokemon_id,                 # Include the Pokémon ID
        'name': pokemon_name,             # Name of the Pokémon
        'type': primary_type,             # Primary type of the Pokémon
        'sprite': sprite,                 # Pokémon sprite
        'hp': data['stats'][0]['base_stat']  # Example: get the base HP stat
    }
