import gridworld as gw
from iagent import IAgent
from gridworld_mc_agent import GridWorldMcAgent

class GridWorldExploler:
    def __init__(self, agent:IAgent, env = gw.GridWorld()) -> None:
        self.env = env
        self.agent = agent
    
    def learn_with_episode(self):
        total_episodes = 1000
        for episode in range(total_episodes):
            state = self.env.reset()
            self.agent.reset()
            
            while True:
                action = self.agent.get_action(state)
                next_state, reward, isGoaled = self.env.step(action)
                
                self.agent.add(state, action, reward)
                if isGoaled:
                    # ゴールしたらその結果を使ってQとpiをアップデート
                    if episode % 100 == 0:
                        self.agent.update()
                        self.env.render_q(self.agent.Q)
                    break
                state = next_state
        self.env.render_q(self.agent.Q)

def main():
    agent = GridWorldMcAgent()
    env = gw.GridWorld()
    env.wall_states = [(1, 1), (0, 1)]
    exploler = GridWorldExploler(agent, env)
    
    exploler.learn_with_episode()


if __name__ ==  "__main__":
    main()