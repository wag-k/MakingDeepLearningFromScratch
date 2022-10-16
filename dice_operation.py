import numpy as np

import dice

class DiceOperation:
    @staticmethod
    def sum_dice_roll(dices = 2) -> int:
        sum = 0
        for _ in range(dices):
            sum += dice.Dice.roll()
        return sum
    

def main():
    totalTryCnt = 10
    for _ in range(10):
        print(DiceOperation.sum_dice_roll())
    
if __name__ == "__main__":
    main()