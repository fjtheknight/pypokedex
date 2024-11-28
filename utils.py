def disable_movement(window):
    window.unbind("<Up>")
    window.unbind("<Down>")
    window.unbind("<Left>")
    window.unbind("<Right>")

def enable_movement(window, move):
    window.bind("<Up>", move)
    window.bind("<Down>", move)
    window.bind("<Left>", move)
    window.bind("<Right>", move)
