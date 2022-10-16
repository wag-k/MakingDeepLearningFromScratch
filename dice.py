import numpy as np

class Dice:
    """Roll the dice

    Returns:
        int: dice roll
    """
    @staticmethod 
    def roll() -> int:
        result : int = np.random.choice([1,2,3,4,5,6])
        return result
    
    