from select import select
from matplotlib.artist import get
import numpy as np

def argmax(xs: iter) -> int:
    """配列の最大値となるインデックスを返します。

    Args:
        xs (iter): 配列。max関数を適用できることが条件

    Returns:
        int: 配列が最大値となるときのインデックス。複数ある場合はランダムでひとつ返す。
    """
    idxes = [i for i, x in enumerate(xs) if x == max(xs)]
    if len(idxes) == 1:
        return idxes[0]
    elif len(idxes) == 0:
        return np.random.choice(len(xs))
    selected_idx = np.random.choice(idxes)
    return selected_idx

def get_greedy_probabilities(Q:dict[tuple], state, epsilon = 0.0, action_size = 4) -> dict[int, float]:
    """Get greedy probalities

    Args:
        Q (dict[tuple]): Action-Value Function
        state (_type_): current_state
        epsilon (float): Greedyな確率分布に重みづけします。
        action_size (int, optional): size of action list. Defaults to 4.

    Returns:
        dict[int, float]: Q関数を最大にするインデックスが選ばれるような確率分布に
        epsilonの重みをつけて返す。
    """
    qs = [Q[(state, action)] for action in range(action_size)]
    max_action = argmax(qs)
    base_probability = epsilon/action_size
    #action_probabilities = {0: ε/4, 1: ε/4, 2: ε/4, 3: ε/4}
    action_probabilities = {action: base_probability for action in range(action_size)}
    # greedy!
    action_probabilities[max_action] += 1 - epsilon
    return action_probabilities

def main():
    test_xs = [0, 1, 2, 1, 2, 0]
    test_cnt = 6
    for _ in range(test_cnt):
        max_idx_in_xs = argmax(test_xs)
        print(max_idx_in_xs)
    
    testQ = {((0,0), 0): 0.2, ((0,0), 1): 0.2, ((0,0), 2): 0.4, ((0,0), 3): 0.2}
    action_probabilities_in_testQ = get_greedy_probabilities(testQ, (0,0))
    print(action_probabilities_in_testQ)
    
if __name__ == "__main__":
    main()