import gridworld as gw
from iagent import IAgent
from gridworld_mc_agent import GridWorldMcAgent

class GridWorldExploler:
    def __init__(self, agent:IAgent, env = gw.GridWorld()) -> None:
        self.env = env
        self.agent = agent
    
    def learn_with_episode(self, total_episodes = 1000, show_times = 5):
        show_timing = total_episodes // show_times
        for episode in range(total_episodes):
            self.explore()
            # ゴールしたらその結果を使ってQとpiをアップデート
            self.agent.update()
            if episode % show_timing == 0:
                print(f"episode: {episode}")
                self.env.render_q(self.agent.Q)
        print(f"episode: {episode}")
        self.env.render_q(self.agent.Q)
        
    def explore(self):
        state = self.env.reset()
        self.agent.reset()
        
        while True:
            action = self.agent.get_action(state)
            next_state, reward, isGoaled = self.env.step(action)
            self.agent.add(state, action, reward)
            if isGoaled:
                return
            state = next_state

def main():
    agent = GridWorldMcAgent()
    env = gw.GridWorld()
    env.wall_states = [(1, 1), (0, 1)]
    exploler = GridWorldExploler(agent, env)
    
    exploler.learn_with_episode()


if __name__ ==  "__main__":
    main()