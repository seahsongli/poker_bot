from collections import Counter
from cards import Card
hand_ranks = [
    "High Card",
    "One Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush",
    "Royal Flush"
]

def evaluate_hand(hand):
    # Hand is a list of Card objects including community cards
    ranks = "23456789TJQKA"
    rank_dict = {r:i for i,r in enumerate(ranks, 2)} # '2' : 2, 'J' : 11

    rank_counts = Counter(card.rank for card in hand)
    suit_counts = Counter(card.suit for card in hand)

    # Check for any combo cards
    
    # Check for flush
    flush = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush = [card for card in hand if hand.suits == suit]

    # Check for straight
    sorted_ranks = sorted((rank_dict[card.rank] for card in hand), reverse = True) # start with largest 
    unique_ranks = sorted(set(sorted_ranks), reverse=True)
    straight = None
    for i in range(len(unique_ranks)-4):
        if unique_ranks[i] - unique_ranks[i+4] == 4:
            straight = unique_ranks[i:i+5]
            break
    
    # There is an edge case where A 2 3 4 5 is also a straight, let us handle it
    if not straight and {2,3,4,5,14}.issubset(unique_ranks):
        straight = [2,3,4,5,14]
    
    # Check for straight flush and royal flush
    if flush:
        flush_ranks = sorted([rank_dict[card.rank] for card in flush], reverse=True)
        for i in range(len(flush_ranks) - 4):
            if flush_ranks[i] == flush_ranks[i+4] == 4:
                if flush_ranks[i] == 14:
                    return "Royal Flush", flush_ranks[i:i+5]
                return "Straight Flush", flush_ranks[i:i+5]
        
    # check for 4 of a kind 
    for rank, count in rank_counts.items():
        if count == 4:
            return "Four of a Kind", rank
    
    # Check for full house
    three_of_a_kind = [rank for rank,count in rank_counts.items() if count==3]
    pairs = [rank for rank,count in rank_counts.items() if count >=2] # do not need to sort, 1 player can only have 1 
    if three_of_a_kind:
        best_three = max(three_of_a_kind, key=lambda r: rank_dict[r])
        remaining_pairs = [rank for rank in pairs if rank!=best_three]
        if remaining_pairs:
            best_pair = max(remaining_pairs, key=lambda r: rank_dict[r])
            return "Full House", (best_three, best_pair)
    
    if flush:
        return "Flush", flush[:5]

    if straight:
        return "straight", straight
    
    if three_of_a_kind:
        best_three = max(three_of_a_kind, key=lambda r: rank_dict[r])
        return "Three of a Kind", best_three
    
    if len(pairs) >= 2:
        best_pairs = sorted(pairs, key=lambda r: rank_dict[r], reverse=True)[:2]
        return "Two Pair", best_pairs

    if pairs:
        best_pair = max(pairs, key=lambda r : rank_dict[r])
        return "Pair", 

    high_card = max(rank_counts.keys(), key = lambda r: rank_dict[r])
    return "High Card", high_card

cards = [
    Card('J', 'Spades'), Card('J', 'Hearts'), Card('J', 'Diamonds'),
    Card('Q', 'Clubs'), Card('T', 'Hearts'), Card('Q', 'Spades'), Card('Q', 'Diamonds')
]
# print(evaluate_hand(cards))  # Output: ('Full House', ('Q', 'J'))