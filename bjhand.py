from hand import *

class BJHand(Hand):

    def __init__(self):
        super().__init__()

    def hasAce(self):
        return self.hasCardWithValue(1)

    def isBusted(self):

    def score(self):
        theScore = 0
        for card in self._cards:
            if card == 10:
                theScore += 10
            else:
                theScore += card
        if card == 1 and theScore <=11:
                theScore += 10
        return theScore

