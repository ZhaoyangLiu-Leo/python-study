#simple text
import simplegui
#define global value
value = 3.14

def convert_units(val, name):
    result = str(val) + ' ' + name
    if val > 1:
        result = result + 's'
    return result

#convert xx.yy to xx dollars and yy cents
def convert(val):
    dollars = int(val)
    cents = round(100 * (val - dollars))
    
    dollars_string = convert_units(dollars, 'dollar')
    cents_string = convert_units(cents, 'cent')
    
    if dollars == 0 and cents == 0:
        return 'Broke!'
    elif(dollars == 0):
        return cents_string
    elif(cents == 0):
        return dollars_string
    else:
        return dollars_string + ' and ' + cents_string

#define canvas_handler
def draw(canvas):
    canvas.draw_text(convert(value), [60, 110], 24, 'White')
    
#define input_handler
def input_handler(text):
    global value
    value = float(text)

frame = simplegui.create_frame('Convert Text', 400, 200)
frame.set_draw_handler(draw)
frame.add_input('Enter value', input_handler, 100)

frame.start()