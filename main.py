import os
import random
import tkinter as tk

import pokedex
from api import get_random_pokemon
from PIL import Image, ImageTk
from utils import disable_movement, enable_movement

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
PLAYER_SIZE = 40
MOVE_STEP = 10
ENCOUNTER_CHANCE = 4  # Percentage chance for an encounter

# Paths
script_dir = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(script_dir, "assets")

# Global state
state = {
    "current_sprite": None,
    "encounter_active": False,
}

# Images and UI
images = {}

def load_images():
    """Load all required images."""
    global images
    # Background and player images
    images["bg"] = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_DIR, "bg.png")))
    player_img = Image.open(os.path.join(ASSETS_DIR, "player2.png")).resize((PLAYER_SIZE, PLAYER_SIZE))
    images["player_left"] = ImageTk.PhotoImage(player_img)
    images["player_right"] = ImageTk.PhotoImage(player_img.transpose(Image.FLIP_LEFT_RIGHT))

def create_canvas(window):
    """Create and return a canvas with the background image."""
    canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.create_image(80, 0, image=images["bg"], anchor="nw")
    canvas.pack()
    return canvas

def setup_player(canvas):
    """Set up the player sprite on the canvas."""
    state["current_sprite"] = images["player_left"]
    return canvas.create_image(400, 200, image=state["current_sprite"])

def move_player(event, canvas, player):
    """Handle player movement and trigger encounters."""
    if state["encounter_active"]:
        return

    x, y = canvas.coords(player)
    move_x, move_y = 0, 0

    if event.keysym == "Down" and y > PLAYER_SIZE-20:
        move_y = -MOVE_STEP
    elif event.keysym == "Left" and y < WINDOW_HEIGHT - PLAYER_SIZE-20:
        move_y = MOVE_STEP
    elif event.keysym == "Right" and x > PLAYER_SIZE+60:
        move_x = -MOVE_STEP
        state["current_sprite"] = images["player_left"]
    elif event.keysym == "Up" and x < WINDOW_WIDTH - PLAYER_SIZE-60:
        move_x = MOVE_STEP
        state["current_sprite"] = images["player_right"]

    canvas.move(player, move_x, move_y)
    canvas.itemconfig(player, image=state["current_sprite"])

    # Trigger encounter randomly
    if random.randint(1, 100) <= ENCOUNTER_CHANCE:
        handle_encounter(canvas)

def handle_encounter(canvas):
    """Handle Pokémon encounters."""
    disable_movement(window)
    state["encounter_active"] = True

    pokemon = get_random_pokemon()
    pokedex.add_to_pokedex(pokemon["id"], pokemon["name"], pokemon["type"], pokemon["hp"], pokemon["sprite"])
    
    # Display encounter dialog
    encounter_window = tk.Toplevel(window)
    encounter_window.title("Wild Pokémon Encounter")
    encounter_window.protocol("WM_DELETE_WINDOW", lambda: end_encounter(encounter_window))

    tk.Label(encounter_window, text=f"You encountered a wild {pokemon['name']}!").pack()
    tk.Label(encounter_window, image=pokemon['sprite']).pack()
    tk.Button(encounter_window, text="Continue", command=lambda: end_encounter(encounter_window)).pack()

def end_encounter(encounter_window):
    """Close encounter window and re-enable movement."""
    encounter_window.destroy()
    state["encounter_active"] = False
    enable_movement(window, lambda e: move_player(e, canvas, player))

# Main Setup
window = tk.Tk()
window.title("BI Pokédex")
load_images()

canvas = create_canvas(window)
player = setup_player(canvas)

pokedex_button = tk.Button(window, text="Open Pokédex", command=lambda: pokedex.display_pokedex(window))
pokedex_button.pack(pady=10)

enable_movement(window, lambda e: move_player(e, canvas, player))
window.mainloop()
