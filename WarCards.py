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
put drawn cards back into their respective deck
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
    def get_hand(self):
        return self.hand
    def update_hand(self, new_hand):
        self.hand = new_hand
        return self.hand


class Round:
    def __init__(self, p1_hand, p2_hand):
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand
        #two randomized hands, total of 52 cards, 26 in each
        #each pulls a card from their respective hand
        #player with the higher card value takes their card and the loser's card and adds it to their pile
    def basic_round(self):
        p1_card = self.p1_hand.pop(0)
        p2_card = self.p2_hand.pop(0)
        print(f"Player 1's card: {p1_card}\nPlayer 2's card: {p2_card}")
        if p1_card[0] > p1_card[0]:
            print("Player 1 wins the round")
            self.p1_hand.extend([p1_card, p2_card])
            return self.p1_hand, self.p2_hand
        elif p1_card[0] < p1_card[0]:
            print("Player 2 wins the round")
            self.p2_hand.extend([p2_card, p1_card])
            return self.p1_hand, self.p2_hand
        else:
            print("Both players' card have the same value: time for War!")
            return self.p1_hand, self.p2_hand
    def war_round(self):
        self.p1_hand.extend(p1_card)
        if (len(self.p1_hand) < 3):
            print("Player 1 does not have enough cards to go to war\n Player 2 wins!")
            return 0
        elif (len(self.p2_hand) < 3):
            print("Player 2 does not have enough cards to go to war\n Player 1 wins!")
            return 0
        else:
            self.p1_hand.append(p1_card)
            p1_war = []
            p2_war = []
            for i in range (0,5):
                p1_war.append(self.p1_hand[i])
                p2_war.append(self.p2_hand[i])
            p1_war_card = p1_war.pop()
            p2_war_card = p2_war.pop()
            print(f"Player 1's war card: {p1_war_card}\nPlayer 2's war card: {p2_war_card}")
            if p1_war_card[0] > p2_war_card[0]:
                print("Player 1 wins the round")
                self.p1_hand.extend([p1_war_card, p1_war, p2_war_card, p2_war])
                return self.p1_hand, self.p2_hand
            elif p1_war_card[0] < p2_war_card[0]:
                print("Player 2 wins the round")
                self.p2_hand.extend([p2_war_card, p2_war, p1_war_card, p1_war])
                return self.p1_hand, self.p2_hand
 


def main():
    current_deck = Deck()
    current_deck.generating_cards()
    current_deck.shuffle_deck()
    name = str(input("Enter your name: "))
    hand1, hand2 = current_deck.deal_deck()
    player1 = Player(name, hand1)
    player2 = Player("Bot", hand2)
    game_begins = input("Are you ready to play War? Enter 'Yes' or 'No': ")
    if game_begins == "Yes":
        print("Let's play!")
        #Need to add in a loop to continue the rounds until game has ended/one player has all cards/war w/o enough cards
        round = Round(player1.get_hand(), player2.get_hand())
        round.basic_round()
        #Continue game loop here 
        
    else:
        #Placeholder for not playing
        print("Maybe next time!")
        



