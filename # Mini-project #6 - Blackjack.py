# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_card_pos = [100, 400]
dealer_card_pos = [100, 200]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        # create Hand object
        self.card_list = []

    def __str__(self):
        # return a string representation of a hand
        s = 'Hand contains'
        for i in range(len(self.card_list)):
            s += ' ' + str(self.card_list[i])
        return s

    def add_card(self, card):
        # add a card object to a hand
        self.card_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        sum_value = 0
        for i in range(len(self.card_list)):
            sum_value += VALUES[self.card_list[i].get_rank()]
        for i in range(len(self.card_list)):
            if self.card_list[i].get_rank() == 'A':
                if sum_value + 10 <= 21:
                    sum_value += 10
                    break
        return sum_value
               
    def draw(self, canvas, pos):
    # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.card_list)):
            self.card_list[i].draw(canvas, [pos[0] + i * 100, pos[1]])
        
class Deck:
    def __init__(self):
        self.card_list = []
        for i in range(4):
            for j in range(13):
                card = Card(SUITS[i], RANKS[j])
                self.card_list.append(card)
        
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.card_list)

    def deal_card(self):
        # deal a card object from the deck
        card = self.card_list.pop()
        return card
    
    def __str__(self):
        # return a string representing the deck
        s = 'Deck contains'
        for i in range(len(self.card_list)):
            s += ' ' + str(self.card_list[i])
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global deck, player, dealer
    if in_play:
        score -= 1
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    in_play = True
    outcome = 'Hit or Stand?'
    
def hit():
    global outcome, in_play, score
    # if the hand is in play, hit the player
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            in_play = False
            score -= 1
            outcome = 'You have busted!'
        
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global in_play, score, outcome
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        # assign a message to outcome, update in_play and score
        in_play = False
        if dealer.get_value() > 21:          
            score += 1
            outcome = 'You win'
        else:
            if player.get_value() > dealer.get_value():
                score += 1
                outcome = 'You win!'
            else:
                score -= 1
                outcome = 'You lose!'
            
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    player.draw(canvas, player_card_pos)
    dealer.draw(canvas, dealer_card_pos)
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [dealer_card_pos[0] + CARD_CENTER[0], dealer_card_pos[1] + CARD_CENTER[1]], CARD_BACK_SIZE)
    else:
        canvas.draw_text('New deal?', (250, 180), 26, 'Black')
    canvas.draw_text('Blackjack', (110, 80), 40, 'Aqua')
    canvas.draw_text('Dealer', (100, 180), 30, 'Black')
    canvas.draw_text('Player', (100, 380), 30, 'Black')
    canvas.draw_text('Score:' + str(score), (450, 100), 30, 'Black')
    canvas.draw_text(outcome, (250, 380), 26, 'Black')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric