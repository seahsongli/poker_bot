class Player:
    def __init__(self, name, stack):
        self.name = name
        self.hand = []
        self.stack = stack
    
    def __repr__(self):
        return f"Player({self.name}, Stack: {self.stack}, Hand: {self.hand})"

    def receive_cards(self, cards):
        self.hand.extend(cards)
    
    def bet(self, amount):
        if amount > self.stack:
            raise ValueError("Cannot bet more than the current stack")
        self.stack-=amount
        return amount

    def raise_bet(self, current_bet, raise_amount):
        total_amount = current_bet + raise_amount 
        if total_amount > self.stack:
            raise ValueError("Cannot bet more than the current stack")
        self.stack-=raise_amount
       
    def fold(self):
        self.hand = []


# player1 = Player("Jack", 1000)
# player1.receive_cards(["Hearts 1", "Spades 2"])
# print(player1)
# player1.bet(100)
# print("Amount of chips left after betting: ", player1.stack)
# player1.raise_bet(100, 300)
# print("Amount of chips left after raising bet: ", player1.stack)
# player1.fold()
# print("Player's hand after folding: ", player1.hand)