"""
Add a Bubble class to the template which has the fields pos (list), vel (list), and color (string).
(Note that this class is similar to the Sprite class for Spaceship.) In this step, implement the following methods
for this class: __init__ creates a bubble whose initial position is the firing position, whose initial velocity is zero
and whose color is generated randomly inside the initializer, update which updates the bubble's position based on its
velocity. Include code in this method to cause the bubble to bounce off of the left and right walls, fire which assigns
a provided non-zero velocity to the bubble when the bubble is fired, and draw which draws the bubble with the given
color at its given position.
"""

# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
bubble_stuck = True


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# class defintion for Bubbles
class Bubble:

    def __init__(self):
        self.pos = list(FIRING_POSITION)
        self.vel = [0, 0]
        self.color = random.choice(COLOR_LIST)

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0]>=WIDTH-BUBBLE_RADIUS or self.pos[0]<=BUBBLE_RADIUS:
            self.vel[0] *= -1


    def fire_bubble(self, vel):
        self.vel = vel

    def is_stuck(self):
        pass

    def collide(self, bubble):
        pass

    def draw(self, canvas):
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 1, self.color, self.color)


# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck
    if simplegui.KEY_MAP["left"] == key:
        firing_angle_vel += FIRING_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC


def keyup(key):
    global firing_angle_vel
    if simplegui.KEY_MAP["left"] == key:
        firing_angle_vel -= FIRING_ANGLE_VEL_INC
    elif simplegui.KEY_MAP["right"] == key:
        firing_angle_vel += FIRING_ANGLE_VEL_INC

# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck

    # update firing angle
    firing_angle += firing_angle_vel

    # draw firing line
    orient = angle_to_vector(firing_angle)
    upper_endpoint = [FIRING_POSITION[0] + FIRING_LINE_LENGTH * orient[0],
                      FIRING_POSITION[1] - FIRING_LINE_LENGTH * orient[1]]
    canvas.draw_line(FIRING_POSITION, upper_endpoint, 4, "White")

    # update a_bubble and check for sticking


    # draw a bubble and stuck bubbles


# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
frame.start()