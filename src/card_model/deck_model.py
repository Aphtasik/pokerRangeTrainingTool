import random
from pydantic import BaseModel

from typing import List

VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
COLORS = ["club", "diamond", "spade", "heart"]


class Card(BaseModel):
    value: str
    color: str


class Deck:
    cards: List[Card]

    def __init__(self) -> None:
        self.cards = [Card(value=v, color=c) for v in VALUES for c in COLORS]
        random.shuffle(self.cards)

    def get_hand(self):
        return (self.cards[0], self.cards[1])

    def get_hand_str(self) -> str:
        x = f"{self.cards[0].value}{self.cards[1].value}"
        if self.cards[0].value == self.cards[1].value:
            return x

        elif self.cards[0].color == self.cards[1].color:
            return x + "s"
        else:
            return x + "o"
