"""
Julianna Della Selva
War!
This program runs through the War card game, as traditionally played
Will be altered to accomodate for strategy in a later project

Basic functionality:

Deck of Cards:
Contains:
The generation of the card deck
Shuffling of the deck
Dealing of the deck
- In War,the deck is split in half

Game (War!):
Basic instructions:
Basic Round:
Players 1 and 2 pick up the first card in their hand
they place it down at the same time
compare the values of the two cards (Ace = 14, the highest)
the player whose card has the greater value wins the round
this player takes their card and the losing player's card (in that order) and puts it at the bottom of their hand
repeat

Special Round (War!)
if both players 1 and 2 place a card of the same value at the same time down
War round begins:
each player places three cards face down
each player then draws a fourth card and places it face up
the face up cards are compared:
if one player has a card that has a greater value than the other
they take all of the cards (theirs then the losing cards)
begin new round
if they tie
begin another War round
if a player does not have enough cards for War:
End game

End game:
once a player has no cards/a player has the full deck or War round case:
player with the full deck wins
player with the empty deck loses


"""

import random
#Deck of Cards
class Deck:
    # Initializing the deck
    def __init__(self):
        self.total_deck = []
        self.num_split = 2
        self.temp_deck = []
        self.houses = ["Hearts", "Diamonds", "Spades", "Clubs"]
        
    # Generating the deck
    def generating_cards(self):
        while self.num_split < 11:
            for suit in self.houses:
                self.temp_deck.append([self.num_split, suit])
            self.num_split += 1

        for suit in self.houses:
            self.temp_deck.append([13, "King", suit])
            self.temp_deck.append([12, "Queen", suit])
            self.temp_deck.append([11, "Jack", suit])
            self.temp_deck.append([14, "Ace", suit])

        for item in self.temp_deck:
            self.total_deck.append(item)
    #Shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.total_deck)
        return self.total_deck
    #deal the deck
    def deal_deck(self):
        return self.total_deck[:26], self.total_deck[26:]
class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    def print_hand(self):
        print(f"{self.name}'s hand includes: {self.hand}\nTotal number of cards: {len(self.hand)}")
"""
class Round:
    def __init__(self):
           
    class War:
        def __init__(self):
"""

def main():
    current_deck = Deck()
    current_deck.generating_cards()
    current_deck.shuffle_deck()
    name = str(input("Enter your name: "))
    hand1, hand2 = current_deck.deal_deck()
    player1 = Player(name, hand1)
    player2 = Player("Bot", hand2)
    player1.print_hand()
    player2.print_hand()

