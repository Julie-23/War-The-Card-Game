#Importing random module for shuffling
import random

#Deck of Cards
#Generating, shuffling, and dealing the deck
class Deck:
    #Initializing the deck
    def __init__(self):
        self.total_deck = []
        self.num_split = 2
        self.temp_deck = []
        self.houses = ["Hearts", "Diamonds", "Spades", "Clubs"]
        
    #Generating the deck
    def generating_cards(self):
        # Number cards 2-10
        for num in range(2, 11):
            for suit in self.houses:
                self.temp_deck.append([num, str(num), suit])
        # Face cards
        for suit in self.houses:
            self.temp_deck.append([11, "Jack", suit])
            self.temp_deck.append([12, "Queen", suit])
            self.temp_deck.append([13, "King", suit])
            self.temp_deck.append([14, "Ace", suit])

        for item in self.temp_deck:
            self.total_deck.append(item)
        return self.total_deck
    
    #Shuffle the deck
    def shuffle_deck(self):
        random.shuffle(self.total_deck)
        return self.total_deck
    #Deal the deck
    def deal_deck(self):
        return self.total_deck[:26], self.total_deck[26:]
    
#Players
#Contains player name and hand
class Player:
    #Initializing player name and hand
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    #Getting player hand
    def get_hand(self):
        return self.hand
    #Updating player hand
    def update_hand(self, new_hand):
        self.hand = new_hand
        return self.hand

#Rounds
#Basic Round and Special Round (War!)
class Round:
    #Initializing player hands
    def __init__(self, p1_hand, p2_hand, spoils, p1_name="", p2_name=""):
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.spoils = []
    #Basic Round functionality
    def basic_round(self):
        if len(self.p1_hand) == 0 or len(self.p2_hand) == 0:
            print("A player has run out of cards. Ending round.")
            return self.p1_hand, self.p2_hand
        p1_card = self.p1_hand.pop(0)
        p2_card = self.p2_hand.pop(0)
        print(f"{self.p1_name}'s card: {p1_card}\n{self.p2_name}'s card: {p2_card}")
        if p1_card[0] > p2_card[0]:
            print(f"{self.p1_name} wins the round")
            self.p1_hand.extend([p1_card, p2_card])
            return self.p1_hand, self.p2_hand
        elif p1_card[0] < p2_card[0]:
            print(f"{self.p2_name} wins the round")
            self.p2_hand.extend([p2_card, p1_card])
            return self.p1_hand, self.p2_hand
        else:
            print("Both players' card have the same value: time for War!")
            if (len(self.p1_hand) < 4):
                print("Player 1 does not have enough cards to go to war\n Player 2 wins!")
                return self.p1_hand, self.p2_hand
            elif (len(self.p2_hand) < 4):
                print("Player 2 does not have enough cards to go to war\n Player 1 wins!")
                return self.p1_hand, self.p2_hand
            else:
                #self.p1_hand.extend([p1_card])
                #self.p2_hand.extend([p2_card])
                self.spoils.extend([p1_card, p2_card])
            return self.war_round(self.p1_hand, self.p2_hand)
    #Special Round (War!) functionality
    def war_round(self, p1_hand, p2_hand):
        p1_warpile = []
        p2_warpile = []
        count = 3
        while count > 0:
            card1 = p1_hand.pop(0)
            card2 = p2_hand.pop(0)
            p1_warpile.append(card1)
            p2_warpile.append(card2)
            count-=1
        p1_warcard = p1_hand.pop(0)
        p2_warcard = p2_hand.pop(0)
        print(f"{self.p1_name}'s war card: {p1_warcard}\n{self.p2_name}'s war card: {p2_warcard}")
        if p1_warcard[0] > p2_warcard[0]:
            print(f"{self.p1_name} wins the round")
            self.p1_hand.extend(self.spoils + p1_warpile + [p1_warcard] + p2_warpile + [p2_warcard])
            self.spoils.clear()
            return self.p1_hand, self.p2_hand
        elif p2_warcard[0] > p1_warcard[0]:
            print(f"{self.p2_name} wins the round")
            self.p2_hand.extend(self.spoils + p2_warpile + [p2_warcard] + p1_warpile + [p1_warcard])
            self.spoils.clear()
            return self.p1_hand, self.p2_hand
        else:
            print("Both players' war card have the same value: time for another War!")
            temp = p1_warpile + [p1_warcard] + p2_warpile + [p2_warcard]
            self.spoils.extend(temp)
            return self.war_round(p1_hand, p2_hand)
            

        
            
#Main function to run the game
def main():
    current_deck = Deck()
    current_deck.generating_cards()
    current_deck.shuffle_deck()
    name1 = str(input("Enter your name: "))
    name2 = str(input("Enter your opponent's name (or leave blank for Bot): "))
    if name2 == "":
        name2 = "Bot"
    hand1, hand2 = current_deck.deal_deck()
    player1 = Player(name1, hand1)
    player2 = Player(name2, hand2)
    game_begins = input("Are you ready to play War? Enter 'Yes' to begin: ")
    if game_begins.upper().strip() == "YES":
        print("Let's play!")
        while len(player1.get_hand()) > 0 and len(player2.get_hand()) > 0:
            current_round = Round(player1.get_hand().copy(), player2.get_hand().copy(), [], name1, name2)
            current_round.basic_round()
            player1.update_hand(current_round.p1_hand)
            player2.update_hand(current_round.p2_hand)
            print(f"{player1.name} has {len(player1.get_hand())} cards left")
            print(f"{player2.name} has {len(player2.get_hand())} cards left")
        if len(player1.get_hand()) == 0:
            print(f"{player2.name} wins the game!")
        elif len(player2.get_hand()) == 0:
            print(f"{player1.name} wins the game!")
    else:
        #Placeholder for not playing
        print("Maybe next time!")


if __name__ == "__main__":
    main()
