from enum import Enum
import random

Cards = Enum("Cards",  ["NonLand", "GoodLand", "BadLand"])


def should_mull(cards, hand_size):
    """ given a set of cards (represented as a dict),
    and hand_size representing the number of cards the player can keep,
    returns True if the player takes a mulligan
    otherwise returns False

    This function will change the dictionary cards
    """

    def remove_land(cards):
        # remove a land from a hand
        if cards[Cards.BadLand] >= 1:
            cards[Cards.BadLand] -= 1
        else:
            cards[Cards.GoodLand] -= 1
            
                
    if hand_size == 7:
        return cards[Cards.NonLand] not in [2,3,4,5]
    if hand_size == 6:
        ## de 2 à 4 lands sur 6 cartes
        ## Donc nonLand de 2 à 4
        if cards[Cards.NonLand] not in [2,3,4,5]:
            return True
            
        if cards[Cards.NonLand] > 3:
            cards[Cards.NonLand] -= 1
            # so either 4 nonlands and  2 lands
            # or 3 nonlands  and 3 lands
        else:
            # either 4 nonlands and  2 lands
            # or 3 nonlands  and 3 lands
            remove_land(cards)
        return False

    if hand_size == 5:
        if cards[Cards.NonLand] in [0,6,7]:
            return True
        if cards[Cards.NonLand] > 3:
            # 4 or 5
            cards[Cards.NonLand] -= 2
        elif cards[Cards.NonLand] == 3:
            # 3 nonlands, 4 lands, we bottom 1 spell, 1 nonland
            remove_land(cards)
            cards[Cards.NonLand] -= 1
        else:
            # 1 nonlands, 6 lands
            # 2 nonlands, 5 lands
            # we bottom 2 lands
            remove_land(cards)
            remove_land(cards)
        return False

    if hand_size == 4:
        # no mull possible
        if cards[Cards.NonLand] > 3:
            cards[Cards.NonLand] -= 3
        elif cards[Cards.NonLand] == 3:
            cards[Cards.NonLand] -= 2
            remove_land(cards)
        elif cards[Cards.NonLand] == 2:
            cards[Cards.NonLand] -= 1
            remove_land(cards)
            remove_land(cards)
        else:
            remove_land(cards)
            remove_land(cards)
            remove_land(cards)
        return False
        


def enough(target_good, target_other, good_lands, total_lands = 25, N = 200000):

    non_lands = 60 - total_lands
    bad_lands = total_lands - good_lands

    success = 0
    fail = 0
    for i in range(N):

        total_cards = 7
        while True:
            deck = [Cards.NonLand]*(non_lands) + [Cards.GoodLand]*good_lands + [Cards.BadLand]*bad_lands
            random.shuffle(deck)
            cards = { card_type : 0 for card_type in Cards }
            for draw in range(7):
                cards[deck.pop()] += 1

            if not should_mull(cards, total_cards):
                break
            total_cards -= 1

        lands_in_play = { card_type : 0 for card_type in Cards }
    
        if cards[Cards.GoodLand] > 0:
            lands_in_play[Cards.GoodLand] += 1
            cards[Cards.GoodLand] -= 1
        elif cards[Cards.BadLand] > 0:
            lands_in_play[Cards.BadLand] += 1
            cards[Cards.BadLand] -= 1
            
        turns = target_good + target_other - 1
        for i in range(turns):
            cards[deck.pop()] += 1
            if cards[Cards.GoodLand] > 0:
                lands_in_play[Cards.GoodLand] += 1
                cards[Cards.GoodLand] -= 1
            elif cards[Cards.BadLand] > 0:
                lands_in_play[Cards.BadLand] += 1
                cards[Cards.BadLand] -= 1
        
        if sum(lands_in_play.values()) == target_good + target_other:
            if lands_in_play[Cards.GoodLand]  >= target_good:
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

for lands in range(8,args.lands+1):
    rate = enough(good, bad, lands, args.lands, 2000)
    if rate < 0.8:
        continue
    rate = enough(good, bad, lands, args.lands, 100000)
    if 100*rate > 89 + turns:
        break
print(lands)





    







