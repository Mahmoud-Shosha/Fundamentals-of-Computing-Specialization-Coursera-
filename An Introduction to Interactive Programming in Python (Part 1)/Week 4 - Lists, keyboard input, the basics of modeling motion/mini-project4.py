# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
paddle2_pos = (HEIGHT / 2) - HALF_PAD_HEIGHT
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left


def spawn_ball(direction):
    global ball_pos, ball_vel
    x = random.randrange(120, 240) / 60
    y = random.randrange(60, 180) / 60
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction:
        ball_vel = [x, -1 * y]
    else:
        ball_vel = [-1 * x, -1 * y]


# define event handlers
def new_game():
    global left_player_score, right_player_score
    left_player_score = 0
    right_player_score = 0
    spawn_ball(RIGHT)


def draw(canvas):
    global paddle1_pos, paddle2_pos
    global left_player_score, right_player_score

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT],
                     1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')

    if ball_pos[1] - BALL_RADIUS <= 0 or ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] *= -1

    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if (paddle1_pos <= ball_pos[1] and
                (paddle1_pos + PAD_HEIGHT) >= ball_pos[1]):
            ball_vel[0] *= -1
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            right_player_score += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if (paddle2_pos <= ball_pos[1] and
                (paddle2_pos + PAD_HEIGHT) >= ball_pos[1]):
            ball_vel[0] *= -1
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            left_player_score += 1
            spawn_ball(LEFT)

    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel > 0 and
            paddle1_pos + paddle1_vel + PAD_HEIGHT < HEIGHT):
        paddle1_pos += paddle1_vel
    if (paddle2_pos + paddle2_vel > 0 and
            paddle2_pos + paddle2_vel + PAD_HEIGHT < HEIGHT):
        paddle2_pos += paddle2_vel

    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos],
                     [HALF_PAD_WIDTH, paddle1_pos+PAD_HEIGHT],
                     PAD_WIDTH, "White")
    canvas.draw_line([WIDTH-HALF_PAD_WIDTH, paddle2_pos],
                     [WIDTH-HALF_PAD_WIDTH, paddle2_pos+PAD_HEIGHT],
                     PAD_WIDTH, "White")

    # determine whether paddle and ball collide

    # draw scores
    canvas.draw_text(str(left_player_score), (WIDTH / 4, HEIGHT / 6),
                     50, 'white')
    canvas.draw_text(str(right_player_score), (3 * WIDTH / 4, HEIGHT / 6),
                     50, 'white')


def keydown(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = +3
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = +3


def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)


# start frame
new_game()
frame.start()
