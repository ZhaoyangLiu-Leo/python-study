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

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == 'Right':
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 2)]
    else:
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 2)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    if RIGHT:
        spawn_ball('Right')
    else:
        spawn_ball('Left')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global LEFT, RIGHT
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] - BALL_RADIUS <= 0:
        ball_vel[1] = -ball_vel[1]        
    elif ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1] 
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] - HALF_PAD_HEIGHT + paddle1_vel >= 0 and paddle1_pos[1] + HALF_PAD_HEIGHT + paddle1_vel <= HEIGHT:
        paddle1_pos[1] += paddle1_vel
    if paddle2_pos[1] - HALF_PAD_HEIGHT + paddle2_vel >= 0 and paddle2_pos[1] + HALF_PAD_HEIGHT + paddle2_vel <= HEIGHT:
        paddle2_pos[1] += paddle2_vel
        
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos[1] - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], [0, paddle1_pos[1] + HALF_PAD_HEIGHT]], 1, 'White', 'White')
    canvas.draw_polygon([[WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], [WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]], 1, 'White', 'White')
    # update scores
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if abs(ball_pos[1] - paddle1_pos[1]) > HALF_PAD_HEIGHT: 
            score2 += 1
            if RIGHT:
                spawn_ball('LEFT')   
                RIGHT = False
                LEFT = True
            else:
                spawn_ball('Right')
                RIGHT = True
                LEFT = False
        else:
            ball_vel[0] = -ball_vel[0] * 1.1       
    elif ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if abs(ball_pos[1] - paddle2_pos[1]) > HALF_PAD_HEIGHT:
            score1 += 1
            if RIGHT:
                spawn_ball('LEFT')
                RIGHT = False
                LEFT = True
            else:
                spawn_ball('Right')
                RIGHT = True
                LEFT = False
        else:
            ball_vel[0] = -ball_vel[0]
        
    # draw scores
    canvas.draw_text(str(score1), [WIDTH /2 - 100, 120], 60, 'White')
    canvas.draw_text(str(score2), [WIDTH /2 + 100, 120], 60, 'White')
    

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5
   
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
    
def restart():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart, 100)


# start frame
new_game()
frame.start()
