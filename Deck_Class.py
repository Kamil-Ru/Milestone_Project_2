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

