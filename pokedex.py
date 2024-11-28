import tkinter as tk

# Initialize an empty list to hold the Pokédex entries
pokedex = []

def add_to_pokedex(pokemon_id, pokemon_name, pokemon_type, pokemon_hp, pokemon_sprite):
    """Add a Pokémon to the Pokédex."""
    new_pokemon = [pokemon_id,pokemon_name, pokemon_type, pokemon_hp, pokemon_sprite]
    pokedex.append(new_pokemon)


def get_all_entries():
    """Retrieve all Pokémon entries in the Pokédex."""
    entries = []
    for pokemon in pokedex:
        id, name, poke_type, hp, sprite = pokemon
        entries.append({
            "id": id,
            "name": name,
            "type": poke_type,
            "hp": hp,
            "sprite": sprite
        })
    return entries

def display_pokedex(window):
    """Display the Pokédex window."""
    pokedex_window = tk.Toplevel(window)
    pokedex_window.title("Pokédex")
    pokedex_window.geometry("900x400")
    
    # TODO: Students should configure the grid and create frames for the Pokédex layout.
    
    # Pokémon list
    pokemon_listbox = tk.Listbox()  # TODO: Complete initialization with correct parent and parameters.
    # TODO: Add the logic to populate `pokemon_listbox` with Pokémon names and IDs.

    pokemon_name = tk.StringVar(value="Select a Pokémon")
    pokemon_type = tk.StringVar(value="Type: ")
    pokemon_hp = tk.StringVar(value="HP: ")
    pokemon_sprite_label = tk.Label()  # TODO: Complete initialization with correct parent and parameters.

    def update_pokemon_details(event):
        # TODO: Add logic to update Pokémon details when a list item is selected.
        pass

    pokemon_listbox.bind("<<ListboxSelect>>", update_pokemon_details)

    # TODO: Add labels to display Pokémon details (name, type, HP, sprite).
