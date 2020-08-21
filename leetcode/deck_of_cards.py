import random

SUITS = ["♦", "♣", "♥", "♠"]
VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    @property
    def suit(self):
        return self.__suit

    @suit.setter
    def suit(self, suit):
        if suit not in SUITS:
            raise Exception("Invalid suit")

        self.__suit = suit

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value not in VALUES:
            raise Exception("Invalid value")

        self.__value = value

    def __repr__(self):
        return f"{self.__value:>2} {self.__suit}"


class Deck:
    def __init__(self):
        cards = [0 for i in range(52)]

        for i in range(len(VALUES)):
            v = VALUES[i]
            for j in range(len(SUITS)):
                s = SUITS[j]

                cards[i * 4 + j] = Card(s, v)

        self.__cards = cards

    def deal(self):
        return self.__cards.pop()

    def shuffle(self):
        random.shuffle(self.__cards)

    def __repr__(self):
        s = ""
        for i in range(0, 52, 4):
            s += str(self.__cards[i:i+4])
            s += "\n"

        return s


deck = Deck()
print(deck)
deck.shuffle()
print(deck)
print(deck.deal())
print(deck)
