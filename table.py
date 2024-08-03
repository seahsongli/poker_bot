class Table:
    def __init__(self, players):
        self.players = players
        self.pot = 0
        self.community_cards = []
    
    def add_to_pot(self, amount):
        self.pot+=amount

    def deal_community_cards(self, cards):
        self.community_cards.extend(cards)
    
    def reset(self):
        self.pot = 0
        self.community_cards = []
