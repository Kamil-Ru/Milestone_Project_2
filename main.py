import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
            
    def __str__(self):
        return self.rank + " of " + self.suit
    
    
class Deck:
    
    def __init__(self,suit,rank):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.deck.append(created_card)
                
       
    def __str__(self):
        string_return = '' 
        for item in range(52):
            string_return = string_return + f'Card in Deck: ' + str(self.deck[item]) + f'\n'
        return string_return

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

test_deck = Deck(suits,ranks)
print(test_deck)


