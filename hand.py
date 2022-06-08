from card import *

class Hand:

    def __init__(self):
        self._cards = []

    @property
    def isEmpty(self):
        return len(self._cards) == 0

    @property
    def numCards(self):
        return len(self._cards)

    def addCard(self, item):
        if isinstance(item, Card):
            self._cards.append(item)
        else:
            raise TypeError(f"Object must be a valid card {type(item)}  {item}")

    def discCard(self, index):
        return self._cards.pop(index)

    def hasCard(self, item):
        if isinstance(item, Card):
            for card in self._cards:
                if card == item:
                    return True
            return False
        else:
            return False

    def hasCardWithSuit(self, suit):
        if isinstance(item, Card):
            for card in self._cards:
                if card.suit == suit:
                    return True
            return False
        else:
            return False

    def hasCardWithValue(self, value):
        if isinstance(item, Card):
            for card in self._cards:
                if card.value == value:
                    return True
            return False
        else:
            return False


    def indexOf(self, item):
        if isinstance(item, Card):
            index = 0
            for card in self._cards:
                if card == item:
                    return index
                index += 1
            return -1
        else:
            return -1

    def __getitem__(self, item):
        """Allows a programmer to [] to peek at a card in the deck"""
        if isinstance(item, int):
            return self._cards[item]
        else:
            raise TypeError(f"Index must an int {type(item)}  {item}")

    def __str__(self):
        """creates a string representation of the cards in the deck"""
        output = f"Hand["
        for c in self._cards:
            output += f"{c} "
        output += "]\n"
        return output

    # def __eq__(self, other):
    #     """ This "magic method" is called when you check the equality of 2 products.  I had to add this to the product class
    #     in order for find and __contains__ to work"""
    #     if isinstance(other, Hand):
    #         return (self.cards == other.cards and self.isEmpty == other.isEmpty and
    #                 self.numCards == other.numCards)
    #     else:
    #         return False


