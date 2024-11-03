from enum import Enum
import numpy as np

array1 = [[1,2,3], [1, 2], [4,5,6], [9], [7,8]]
for a in array1:
    print(a)



class Player:
    couldHaves = []
    mustHaves = []
    dontHaves = []

    def __init__(self, numCards):
        self.numCards = numCards
    
    def addCouldHaves(self, guessShown):
        # Add potentially held cards
        self.couldHaves.append(guessShown)

    def addDontHaves(self, skippedCards):
        # append list of cards that is confirmed this player does NOT have because they failed to show any cards on a guess
        for card in skippedCards:
            self.dontHaves.append(card)
        self.dontHaves = list(set(self.dontHaves)) # keep unique donthaves

    def resolveCouldHaves(self, knownCards):
        # remove could haves that exist in the known card deck
        # remove could haves that are in this players known dont haves
        # search for shown guesses that only have one remaing 
        for guess in self.couldHaves:
            for element in guess:
                if element in knownCards:
                    self.couldHaves.remove(guess)
                if element in self.dontHaves:
                    guess.remove(element)  
            if len(guess) == 1:
                self.addMustHaves(guess[0])
                self.couldHaves.remove(guess)
 
    def addMustHaves(self, knownCard):
        self.mustHaves.append(knownCard)

    def getMustHaves(self):
        return self.mustHaves






class Weapon(Enum):
    CANDLESTICK    = 0
    ROPE = 1
    KNIFE  = 2
    LEADPIPE   = 3
    REVOLVER  = 4
    WRENCH  = 5


class Suspect(Enum):
    MUSTARD  = 0
    PLUM     = 1
    SCARLETT = 2
    PEACOCK  = 3
    WHITE    = 4
    GREEN    = 5   

class Room(Enum):
    BILLIARD = 0
    STUDY = 1
    HALL  = 2
    LOUNGE   = 3
    DININGROOM  = 4
    BALLROOM  = 5
    CONSERVATORY= 6  
    LIBRARY = 7
    KITCHEN = 8
