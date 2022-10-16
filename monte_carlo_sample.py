import numpy as np

import dice_operation as diceop

def calc_sum_dice_roll_expectation_by_monte_carlo(dices = 2, total_trial = 1000):
    expectation, n = 0, 0
    for _ in range(total_trial):
        s = diceop.DiceOperation.sum_dice_roll(dices=dices)
        n += 1
        expectation += (s - expectation) / n
    return expectation

def main():
    e = calc_sum_dice_roll_expectation_by_monte_carlo(2, 10000)
    print(e)

if __name__ ==  "__main__":
    main()