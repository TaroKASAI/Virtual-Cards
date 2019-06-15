import random

class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def __repr__(self):
        return "{}:{}".format(self.suit, self.number)

class Deck():
    suits = ["Spade", "Heart", "Diamond", "Clover"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for number in self.numbers:
                card = Card(suit, number)
                self.cards.append(card)
    ##This __init__ creates 52 cards for a deck.
    def shuffle(self):
        self.new_cards = []
        for i in range(52):
            random_card = random.choice(self.cards)
            self.cards.remove(random_card)
            self.new_cards.append(random_card)
        self.cards = self.new_cards

class Player():
    def __init__(self):
        self.cards = []
    def draw(self, deck, draw_number=1):
        for i in range(draw_number):
            drawed_card = deck.cards.pop()
            self.cards.append(drawed_card)
    #draw a card from "deck" "number" times
    def give(self, deck, card):
        self.cards.remove(card)
        deck.cards.append(card)
    #give a "card" to "deck"


the_deck = Deck()
the_deck.shuffle()

me = Player()
bob = Player()
me.draw(the_deck,5)
bob.draw(the_deck,5)

print(me.cards)
chosen_card = input("Which card do you wannna give bob?\n")
me.give(bob,chosen_card)
print(me.cards)
print(bob.cards)
