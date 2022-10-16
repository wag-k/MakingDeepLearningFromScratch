import matplotlib.pyplot as plt

def plot_total_reward(reward_history):
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.plot(range(len(reward_history)), reward_history)
    plt.show()
    
    
def main():
    test_reward_history = [0., 0.5, 1.]
    plot_total_reward(test_reward_history)


if __name__ == "__main__":
    main()