import numpy as np
import gridworld_render as render_helper

class GridWorld:
    def __init__(self):
        self.action_space = [0, 1, 2, 3]
        self.action_meaning = {
            0: "UP",
            1: "DOWN",
            2: "LEFT",
            3: "RIGHT",
        }
        
        self.reward_map = np.array(
            [[0, 0, 0, 1.0],
             [0, None, 0, -1.0],
             [0, 0, 0, 0]]
        )

        self.goal_state = (0, 3)
        # 壁が一つとはかぎらないため、配列にしておいたほうが筋がいいと思う。
        self.wall_states = [(1, 1)]
        self.start_state = (2, 0)
        self.agent_state = self.start_state
        
        self.__action_move_map = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    @property
    def height(self):
        return len(self.reward_map)
    
    @property
    def width(self):
        return len(self.reward_map[0])
    
    @property
    def shape(self):
        return self.reward_map.shape
    
    def get_actions(self) -> list:
        return self.action_space
    
    def get_states(self) -> iter:
        for h in range(self.height):
            for w in range(self.width):
                yield (h, w)
        
    def get_next_state(self, state, action):
        next_state = self.__calc_next_state(state, action)
        if not self.check_movable(next_state):
            next_state = state
        return next_state
        
    def __calc_next_state(self, state, action) -> tuple:
        move = self.__action_move_map
        next_state = (state[0] + move[0], state[1] + move[1])
        return next_state

    def check_movable(self, state) -> bool:
        x = state[0]
        y = state[1]
        if x < 0 or self.width <= x or y < 0 or self.height <= y:
            return False
        else:
            for wall in self.wall_states:
                if state == wall:
                    return False
        return True
    
    def get_reward(self, state, action, next_state):
        return self.reward_map[next_state]
    
    def reset(self):
        self.agent_state = self.start_state
        return self.agent_state

    def step(self, action):
        state = self.agent_state
        next_state = self.get_next_state(state, action)
        reward = self.get_reward(state, action, next_state)
        done = (next_state == self.goal_state)

        self.agent_state = next_state
        return next_state, reward, done
    
    def render_v(self, v=None, policy=None, print_value=True):
        renderer = render_helper.Renderer(self.reward_map, self.goal_state,
                                          self.wall_states)
        renderer.render_v(v, policy, print_value)

    def render_q(self, q=None, print_value=True):
        renderer = render_helper.Renderer(self.reward_map, self.goal_state,
                                          self.wall_states)
        renderer.render_q(q, print_value)

def main():
    env = GridWorld()

    print(env.height)
    print(env.width)
    print(env.shape)
    print("Actions:")    
    for action in env.get_actions():
        print(action)
    print("States:")
    for state in env.get_states():
        print(state)
    
    env.render_v()

if __name__ == "__main__":
    main()
