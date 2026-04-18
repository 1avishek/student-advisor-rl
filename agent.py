# agent.py
import numpy as np

class QLearningAgent:
    def __init__(self, n_states, n_actions, lr=0.1, gamma=0.9, epsilon=0.2):
        self.q_table = np.zeros((n_states, n_actions))
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon

    def choose_action(self, state_index):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.q_table.shape[1])
        return np.argmax(self.q_table[state_index])

    def update(self, state_idx, action_idx, reward):
        best_next = np.max(self.q_table[state_idx])
        self.q_table[state_idx, action_idx] += self.lr * (reward + self.gamma * best_next - self.q_table[state_idx, action_idx])
