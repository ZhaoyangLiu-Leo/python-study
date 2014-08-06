# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100
choice = 0
time_guess = 0

# helper function to start and restart the game
def new_game():
    print ''
    global num_range, time_guess
    if(choice == 0):
        num_range = random.randrange(0, 100)
        #compute min-time to gurantee guessing correct result
        time_float = math.log(100 - 0 + 1, 2)
        time_guess = int(math.ceil(time_float))
        print 'New game. Range is from 0 to 100'
        print 'Number of remaining guesses is', time_guess
    elif(choice == 1):
        num_range = random.randrange(0, 1000)
        time_float = math.log(1000 - 0 + 1, 2)
        time_guess = int(math.ceil(time_float))
        print 'New game. Range is from 0 to 1000'
        print 'Number of remaining guesses is', time_guess
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global choice
    choice = 0
    new_game()
    


def range1000():
    # button that changes range to range [0,1000) and restarts
    global choice
    choice = 1
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here
    global num_range, time_guess
    print ''
    num_guess = int(guess)
    time_guess -= 1
    if(time_guess < 0):
        print 'You have used up your guess times!'
        print 'Welcome to paly again'
        new_game()
    else:
        print 'Guess was', num_guess
        print 'Number of remaining guesses is', time_guess
        if(num_guess == num_range):
            print 'Correct!'
            new_game()   
        elif(num_guess > num_range):
            print 'Lower!'
        else:
            print 'Higher!'
    

    
# create frame
frame = simplegui.create_frame('Guess the number!', 200, 200)


# register event handlers for control elements
frame.add_button('Range is [0, 100)', range100, 200)
frame.add_button('Range is [0, 1000)', range1000, 200)
frame.add_input('Enter a guess', input_guess, 200)


# call new_game and start frame
new_game()
frame.start()

