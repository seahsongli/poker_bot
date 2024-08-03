import random
class Card:
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    rank = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        print(f"Card(suit = {self.suit}, rank = {self.rank})")

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.rank]
        random.shuffle(self.cards)

    def deal_cards(self, num_cards):
        if num_cards * 2 > len(self.cards):
            raise ValueError("Not enough cards in deck to deal.")
        return [self.cards.pop() for _ in range(num_cards)]