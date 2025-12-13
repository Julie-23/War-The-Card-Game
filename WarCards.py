#Importing random module for shuffling
import random

#Deck of Cards
#Generating, shuffling, and dealing the deck
class Deck:
    #Initializing the deck
    def __init__(self):
        self.total_deck = []
        self.temp_deck = []
        self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        
    #Generating the deck
    def generating_cards(self):
        self.temp_deck = []
        self.total_deck = []
        # Number cards 2-10
        for num in range(2, 11):
            for suit in self.suits:
                self.temp_deck.append([num, str(num), suit])
        # Face cards
        for suit in self.suits:
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
    def __init__(self,p1_hand, p2_hand, p1_name, p2_name):
        self.p1_hand = p1_hand
        self.p2_hand = p2_hand
        self.p1_name = p1_name
        self.p2_name = p2_name
    #Basic Round
    def basic_round(self):
        if len(self.p1_hand) == 0 or len(self.p2_hand) == 0:
            return self.p1_hand, self.p2_hand
        p1_card = self.p1_hand.pop(0)
        p2_card = self.p2_hand.pop(0)
        print(f"{self.p1_name}'s card: {p1_card[1]} of {p1_card[2]}\n{self.p2_name}'s card: {p2_card[1]} of {p2_card[2]}")
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
            spoils = [p1_card, p2_card]
            return self.war_round(spoils)
        
    #War Round
    def war_round(self, current_spoils):
        if len(self.p1_hand) < 4:
            print(f"{self.p1_name} does not have enough cards to go to war\n {self.p2_name} wins!")
            self.p2_hand.extend(current_spoils)
            self.p2_hand.extend(self.p1_hand)
            self.p1_hand.clear()
            return self.p1_hand, self.p2_hand

        elif len(self.p2_hand) < 4:
            print(f"{self.p2_name} does not have enough cards to go to war\n {self.p1_name} wins!")
            self.p1_hand.extend(current_spoils)
            self.p1_hand.extend(self.p2_hand)
            self.p2_hand.clear()
            return self.p1_hand, self.p2_hand
        
        #Each player places three cards face down
        for i in range(3):
            current_spoils.append(self.p1_hand.pop(0))
            current_spoils.append(self.p2_hand.pop(0))
        #Each player places one card face up
        p1_war_card = self.p1_hand.pop(0)
        p2_war_card = self.p2_hand.pop(0)

        #Add war cards to spoils
        current_spoils.append(p1_war_card)
        current_spoils.append(p2_war_card)

        #Compare war cards and determine winner
        print(f"{self.p1_name}'s war card: {p1_war_card[1]} of {p1_war_card[2]}\n{self.p2_name}'s war card: {p2_war_card[1]} of {p2_war_card[2]}")
        if p1_war_card[0] > p2_war_card[0]:
            print(f"{self.p1_name} wins the war round")
            self.award_spoils(self.p1_hand, current_spoils)
            return self.p1_hand, self.p2_hand

        if p2_war_card[0] > p1_war_card[0]:
            print(f"{self.p2_name} wins the war round")
            self.award_spoils(self.p2_hand, current_spoils)
            return self.p1_hand, self.p2_hand

        #In case of another tie
        print("War cards have tied! Another war begins!")
        return self.war_round(current_spoils)

    #Award spoils to the winner
    def award_spoils(self, winner_hand, spoils):
        winner_hand.extend(spoils)
        return
            
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
        #Game loop
        while len(player1.get_hand()) > 0 and len(player2.get_hand()) > 0:
            current_round = Round(player1.get_hand(), player2.get_hand(), name1, name2)
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
