import random
import numpy as np

class StudentAdvisorEnv:
    def __init__(self, df, subject2id, cost2id):
        self.df = df.reset_index(drop=True)
        self.n_actions = len(self.df)
        self.subject2id = subject2id
        self.cost2id = cost2id
        # Bins to encode IELTS into discrete states
        self.ielts_bins = [6.0, 6.5, 7.0]

    def reset(self):
        # Sample a random student profile
        self.ielts = random.choice([5.5, 6.0, 6.5, 7.0])
        self.budget = random.choice(list(self.cost2id.keys()))
        self.subject = random.choice(list(self.subject2id.keys()))
        # Return the encoded state tuple
        return self._encode_state()

    def _encode_state(self):
        # Convert continuous IELTS to an integer bin
        i_bin = sum(self.ielts > b for b in self.ielts_bins)
        return (i_bin,
                self.cost2id[self.budget],
                self.subject2id[self.subject])

    def step(self, action, reward_fn):
        # Look up the chosen university
        uni = self.df.iloc[action]
        # Call the reward function you’ll build later
        reward = reward_fn(
            student=(self.ielts, self.budget, self.subject),
            university=(uni.Country, uni.University, uni.Subject)
        )
        # Sample a new student for the next state
        next_state = self.reset()
        return next_state, reward
