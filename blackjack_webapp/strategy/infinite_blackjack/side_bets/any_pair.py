
import random
import math
import pandas as pd
import numpy as np
import scipy.stats as st


"""
# Any Pair - side bet calculation

The goal is to receive a pair in the first two cards that you are dealt
- Shoe consists of eight decks
- A suited (perfect) pair pays 25 units
- An unsuited pair pays 8 units
"""


def nCr(n, r):
    """calculates number of combinations (without replacement)"""
    if r > n:
        return 0
    
    f = math.factorial
    return int(f(n) / (f(r) * f(n-r)))
    
# make sure function can do vectorized operations
nCr = np.vectorize(nCr)




# number of possible winning pair combinations
probdf.loc[:, 'All_winning_pairs'] = nCr(probdf['Total_cards'], 2)

# calculate number of suited pair combinations
probdf['Suited_pairs'] = 0
for suit in suits:
    probdf.loc[:, 'Suited_pairs'] += nCr(probdf.loc[:, suit], 2)

# calculate unsuited pairs
probdf['Unsuited_pairs'] = probdf.All_winning_pairs - probdf.Suited_pairs




# total cards in deck and total 2 card combinations
total_cards = sum(probdf.Total_cards)
total_combinations = nCr(total_cards, 2)

prob_suited_pair = sum(probdf.Suited_pairs) / total_combinations
prob_unsuited_pair = sum(probdf.Unsuited_pairs) / total_combinations
prob_losing_pair = 1 - prob_suited_pair - prob_unsuited_pair
print("prob_suited_pair", prob_suited_pair)
print("prob_unsuited_pair", prob_unsuited_pair)
print("prob_losing_pair", prob_losing_pair)
print("-----------------------")

suited_pair_payout = 25
unsuited_pair_payout = 8

return_suited_pair = prob_suited_pair * suited_pair_payout
return_unsuited_pair = prob_unsuited_pair * unsuited_pair_payout
return_losing_pair = -prob_losing_pair

total_ev = return_suited_pair + return_unsuited_pair + return_losing_pair

print("total_ev", total_ev)
