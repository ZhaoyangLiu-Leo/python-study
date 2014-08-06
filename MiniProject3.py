# template for "Stopwatch: The Game"
import simplegui
# define global variables
count = 0
total_time = 0
right_time = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a, b, c, d = 0, 0, 0, 0
    d = t % 10
    t /= 10
    if count < 6000:
        if count >= 10:
            c = t % 10
            t /= 10
        if count >= 100:
            b = t % 6
            t /= 6
        if count >= 600:
            a =  t % 10
    else:
        print 'Over time, timer reset!'
    return str(a) + ':' + str(b) + str(c) +'.' + str(d)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_running
    if  is_running == False:
        is_running = True
        timer.start()

def stop():
    global total_time, right_time, is_running
    if is_running:
        total_time += 1
        is_running = False
        if count % 10 == 0:
            right_time += 1
        timer.stop()
        
def reset():
    global count, total_time, right_time
    timer.stop()
    is_running = False
    count = 0
    total_time = 0
    right_time = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(count), [100, 110], 40, 'White')
    canvas.draw_text(str(right_time) + '/' + str(total_time), [250, 20], 25, 'Green')
        
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 200)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)
# register event handlers
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
