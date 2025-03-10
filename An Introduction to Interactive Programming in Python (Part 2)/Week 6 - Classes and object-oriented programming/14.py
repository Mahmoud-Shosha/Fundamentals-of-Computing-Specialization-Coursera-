"""
Your next task is to build a simple version of Memory that exposes tiles in response to mouse clicks. Using
the provided template, add code to the mouse handler mouseclick() that exposes a tile in response to a mouse click on
that tile. This code should interact with a tile using only Tile class methods.
"""

# Build clickable version of Memory using the Tile class

#################################################
# Student adds code where appropriate

import simplegui
import random

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100
DISTINCT_TILES = 8


# helper function to initialize globals
def new_game():
    global my_tiles, state, turns

    tile_numbers = range(DISTINCT_TILES) * 2
    random.shuffle(tile_numbers)
    my_tiles = [Tile(tile_numbers[i], False, [TILE_WIDTH * i, TILE_HEIGHT]) for i in range(2 * DISTINCT_TILES)]

    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))


# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

        # draw method for tiles

    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_loc = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.get_number()), text_loc, TILE_WIDTH, 'white')
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, 0], [loc[0], 0])
            canvas.draw_polygon(tile_corners, 2, 'gray', 'green')

    # selection method for tiles
    def is_selected(self, pos):
        inside_hor = self.location[0] <= pos[0] < self.location[0] + TILE_WIDTH
        inside_vert = self.location[1] - TILE_HEIGHT <= pos[1] <= self.location[1]
        return inside_hor and inside_vert

    # define event handlers


def mouseclick(pos):
    for tile in my_tiles:
        if tile.is_selected(pos):
            tile.expose_tile()


# add code here

# draw handler
def draw(canvas):
    for tile in my_tiles:
        tile.draw_tile(canvas)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * DISTINCT_TILES * TILE_WIDTH, TILE_HEIGHT)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# get things rolling
new_game()
frame.start()

###################################################
# Clicking on tile should flip them once
