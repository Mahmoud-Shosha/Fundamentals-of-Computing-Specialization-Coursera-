"""
Modify the following program template to print "It works!" on the canvas.
"""


# Print to canvas

###################################################
# Student should add code where relevant to the following.

import simplegui

# Draw handler


def draw(canvas):
    canvas.draw_text("It works!", [120, 112], 48, "Red")


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)

# Register event handlers
frame.set_draw_handler(draw)

# start the frame
frame.start()
