from hand import *

def testConstructor():
    d = Hand()
    print(f"Testing constructor.  Expect 0 cards. {d}")
    print(f"Expect numDominos property to be 0. {d.numCards}")
    print(f"Expect isEmpty property to be true. {d.isEmpty}")

def addCard():
    d = Hand()
    print(f"Testing draw. Expect 0 cards. {d}")
    print(f"Expect numDominos property to be 0. {d.numCards}")
    print(f"Expect isEmpty property to be true. {d.isEmpty}")
    d = d.addCard()
    print(f"after call to deal.  Expect 91 dominos. {d}")
    print(f"Expect numDominos property to be 91. {d.numCards}")
    print(f"Expect isEmpty property to be false. {d.isEmpty}")
    print(f"Expect dealt card to be Ace of Clubs. {d}")
    for i in range(d.numCards):
        d = d.addCard()
    print(f"Dealt the remaining cards.  Expect empty deck. {d}")
    print(f"Expect numCards property to be 0. {d.numCards}")
    print(f"Expect isEmpty property to be true. {d.isEmpty}")