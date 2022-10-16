from collections import defaultdict
import numpy as np

import gridworld as gw
import greedy
from iagent import IAgent

class GridWorldMcAgent(IAgent):
    def __init__(self) -> None:
        # discount rate
        self.gamma = 0.9
        # epsilon-greedy
        self.epsilon = 0.1
        # fixed-alpha value method
        self.alpha = 0.1
        self.action_size = 4
        
        random_actions = {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}
        # policy probability
        self.pi = defaultdict(lambda: random_actions)
        # State-Action Function
        self.Q = defaultdict(lambda: 0)
        # step毎の(state, action, reward)を保存します。
        self.__memory : list[tuple] = []
        
    def get_action(self, state:tuple):
        action_probs = self.pi[state]
        actions = list(action_probs.keys())
        probabilities = list(action_probs.values())
        return np.random.choice(actions, p=probabilities)
    
    def add(self, state, action, reward):
        data = (state, action, reward)
        self.__memory.append(data)
    
    def reset(self):
        self.__memory.clear()
    
    def update(self) -> None:
        # total reward
        G = 0
        for data in reversed(self.__memory):
            state, action, reward = data
            # 後ろから計算することでこの漸化式が適用できるため、
            # 収益の計算コスト削減が可能となる。
            G = self.gamma * G + reward
            key = (state, action)
            # update the Action-State Function
            self.Q[key] += (G - self.Q[key]) * self.alpha
            # update policy probabilities
            self.pi[state] = greedy.get_greedy_probabilities(self.Q, state, self.epsilon)

def main():
    env = gw.GridWorld()
    env.wall_states = [(1, 1), (0, 1)]
    
    agent = GridWorldMcAgent()
    agent.epsilon
    
    total_episodes = 1000
    for episode in range(total_episodes):
        state = env.reset()
        agent.reset()
        
        while True:
            action = agent.get_action(state)
            next_state, reward, isGoaled = env.step(action)
            
            agent.add(state, action, reward)
            if isGoaled:
                # ゴールしたらその結果を使ってQとpiをアップデート
                if episode % 100 == 0:
                    agent.update()
                    env.render_q(agent.Q)
                break
            state = next_state
    env.render_q(agent.Q)

if __name__ ==  "__main__":
    main()
