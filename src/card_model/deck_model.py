import random
from pydantic import BaseModel

from typing import List

COLORS = ["club", "diamond", "spade", "heart"]
VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Card(BaseModel):
    color: str
    value: str


class Deck(BaseModel):
    deck: List[Card]

    def __init__(self):
        self.deck = []
        for color in COLORS:
            for value in VALUES:
                self.deck.append(Card(color, value))
        random.shuffle(self.deck)
