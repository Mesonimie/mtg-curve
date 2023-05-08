
import sys
from random import randrange
from dataclasses import dataclass

@dataclass
class Deck:
    NonLand: int = 0
    GoodLand: int = 0
    BadLand: int = 0
    
    def sum(self):
        return self.NonLand + self.GoodLand + self.BadLand

    def remove_land(self):
        # remove a land from a hand
        if self.BadLand >= 1:
            self.BadLand -= 1
        else:
            self.GoodLand -= 1
    
    
    def get_random_card(self,hand):
        """ returns a random card from a deck
        """
        deck_size = self.sum()
        which = randrange(deck_size)

        if self.NonLand > which:
            self.NonLand -= 1
            hand.NonLand += 1
            return
        which -= self.NonLand
        if self.GoodLand > which:
            self.GoodLand -= 1
            hand.GoodLand += 1
            return
        self.BadLand -= 1
        hand.BadLand += 1
    

        
    
def should_mull(cards, hand_size):
    """ given a set of cards (represented as a dict),
    and hand_size representing the number of cards the player can keep,
    returns True if the player takes a mulligan
    otherwise returns False

    This function will change the dictionary cards
    """

            
                
    if hand_size == 7:
        return cards.NonLand not in [2,3,4,5]
    if hand_size == 6:
        ## de 2 à 4 lands sur 6 cartes
        ## Donc nonLand de 2 à 4
        if cards.NonLand not in [2,3,4,5]:
            return True
            
        if cards.NonLand > 3:
            cards.NonLand -= 1
            # so either 4 nonlands and  2 lands
            # or 3 nonlands  and 3 lands
        else:
            # either 4 nonlands and  2 lands
            # or 3 nonlands  and 3 lands
            cards.remove_land()
        return False

    if hand_size == 5:
        if cards.NonLand in [0,6,7]:
            return True
        if cards.NonLand > 3:
            # 4 or 5
            cards.NonLand -= 2
        elif cards.NonLand == 3:
            # 3 nonlands, 4 lands, we bottom 1 spell, 1 nonland
            cards.remove_land()
            cards.NonLand -= 1
        else:
            # 1 nonlands, 6 lands
            # 2 nonlands, 5 lands
            # we bottom 2 lands
            cards.remove_land()
            cards.remove_land()
        return False

    # hand_size == 4:
    # no mull possible
    if cards.NonLand > 3:
        cards.NonLand -= 3
    elif cards.NonLand == 3:
        cards.NonLand -= 2
        cards.remove_land()
    elif cards.NonLand == 2:
        cards.NonLand -= 1
        cards.remove_land()
        cards.remove_land()
    else:
        cards.remove_land()
        cards.remove_land()
        cards.remove_land()
    return False

def enough(target_good, target_other, good_lands, total_lands = 25, N = 200000):
    deck = Deck()
    cards = Deck()
    lands_in_play = Deck()

    non_lands = 60 - total_lands
    bad_lands = total_lands - good_lands

    success = 0
    fail = 0
    turns = target_good + target_other 

    while N > 0 :

        total_cards = 7
        while True:
            deck.NonLand = non_lands
            deck.GoodLand = good_lands
            deck.BadLand = bad_lands

            cards.NonLand = cards.GoodLand = cards.BadLand = 0
            for draw in range(7):
                deck.get_random_card(cards)

            if not should_mull(cards, total_cards):
                break
            total_cards -= 1

        #no need: lands_in_play.NonLand = 0
        lands_in_play.GoodLand = 0
        lands_in_play.BadLand = 0
    
        if cards.GoodLand > 0:
            lands_in_play.GoodLand += 1
            cards.GoodLand -= 1
        elif cards.BadLand > 0:
            lands_in_play.BadLand += 1
            cards.BadLand -= 1
            
        for i in range(1, turns):
            deck.get_random_card(cards)
            if cards.GoodLand > 0:
                lands_in_play.GoodLand += 1
                cards.GoodLand -= 1
            elif cards.BadLand > 0:
                lands_in_play.BadLand += 1
                cards.BadLand -= 1
            else:
                # no need to get the next cards if we don't have the right number of lands anyway                
                break
        if lands_in_play.sum() == turns:
            N-=1
            if lands_in_play.GoodLand  >= target_good:
                success += 1
            else:
                fail += 1
    return success/(success+fail)
        
    


    

import sys
import argparse

parser = argparse.ArgumentParser(description='curve')

parser.add_argument('cost', type=str, help='Mana Cost (ex: 1CC) should be less than 10 mana value')
parser.add_argument('--lands', metavar='lands', required=False, default=25, type=int, help='Number of lands')

args = parser.parse_args()

good = 0
bad = 0
cost = args.cost
while 'C' in cost :
    cost = cost[:-1]
    good += 1
if len(cost) == 0:
    bad = 0
else:
    bad = int(cost)
turns = good+bad

for lands in range(6,args.lands+1):
    rate = enough(good, bad, lands, args.lands, 1000)
    # if n = 1000 and p > 0.9 then by Chernoff's inequality
    # P(rate < 0.89) < 10^(-18) so is negligible
    if rate < 0.89:
        continue
    rate = enough(good, bad, lands, args.lands, 5000000)
    if 100*rate > 89 + turns:
        break
print(lands, end="")





    







