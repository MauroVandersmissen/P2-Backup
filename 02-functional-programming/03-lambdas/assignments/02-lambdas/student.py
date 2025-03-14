from util import *

cards = [
    Card(value=2, suit='hearts'),
    Card(value=5, suit='clubs'),
    Card(value=10, suit='hearts'),
    Card(value=2, suit='spades'),
    Card(value=4, suit='diamonds'),
    Card(value=5, suit='spades'),
]

def group_by_suit(cards):
    return group_by(cards,lambda card:card.suit)

def group_by_value(cards):
    return group_by(cards,lambda card:card.value)

def partition_by_color(cards):
    return partition(cards,lambda card:card.suit in ["spades","clubs"])

print(group_by_suit(cards))
print(group_by_value(cards))
black_cards,red_cards=partition_by_color(cards)
print(partition_by_color(cards))