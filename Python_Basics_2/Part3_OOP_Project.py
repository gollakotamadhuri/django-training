#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.deck = [(s, r) for s in SUITE for r in RANKS]
        print("Deck Created")

    def shuffle_deck(self):
        random.shuffle(self.deck)
        print("Deck shuffled")
    
    def cut_deck(self):
        return (self.deck[:26], self.deck[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add_cards(self, new_cards):
        self.cards.extend(new_cards)

    def remove_card(self):
        return self.cards.pop()
    
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        card = self.hand.remove_card()
        print("Card played by {} is {} \n".format(self.name, card))
        return card
    
    def draw_war_cards(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards


    def check_cards(self):
        return len(self.hand.cards) !=0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
d = Deck()
d.shuffle_deck()
deck1, deck2 = d.cut_deck()

h1 = Hand(deck1)
h2 = Hand(deck2)

player1_name = input("Enter player one name: ")
player1 = Player(player1_name,h1)

player2_name = input("Enter player two name: ")
player2 = Player(player2_name,h2)

rounds=0
war_rounds=0

while player1.check_cards() and player2.check_cards():
    rounds=rounds + 1
    print("Round {}".format(rounds))
    print("Current standings")

    print("Player1:",player1.hand.__str__())
    print("Player2:",player2.hand.__str__())

    print("{} draws a card".format(player1.name))
    player1_draw = player1.play_card()
    print(player1_draw)
    print("{} draws a card".format(player2.name))
    player2_draw = player2.play_card()
    print(player2_draw)

    table_cards=[]

    table_cards.append(player1_draw)
    table_cards.append(player2_draw)


    if player1_draw[1] == player2_draw[1]:
        war_rounds = war_rounds + 1
        print("War time!")

        table_cards.extend(player1.draw_war_cards())
        table_cards.extend(player2.draw_war_cards())

        if player1.check_cards() and player2.check_cards():


            player1_draw = player1.play_card()
            player2_draw = player2.play_card()

            table_cards.append(player1_draw)
            table_cards.append(player2_draw)

            if RANKS.index(player1_draw[1]) < RANKS.index(player2_draw[1]):
                player2.hand.add_cards(table_cards)
            else:
                player1.hand.add_cards(table_cards)
        else:
            break
    else:
        if RANKS.index(player1_draw[1]) < RANKS.index(player2_draw[1]):
            player2.hand.add_cards(table_cards)
        else:
            player1.hand.add_cards(table_cards)

print("Total rounds played: ",rounds)
print("War happened {} times".format(war_rounds))
print("Final card count for {}".format(player1.name))
print(len(player1.hand.cards))
print("Final card count for {}".format(player2.name))
print(len(player2.hand.cards))



