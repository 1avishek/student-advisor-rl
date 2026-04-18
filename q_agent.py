import random
import numpy as np

class StudentAdvisorEnv:
    def __init__(self):
        self.students = [
            {'name': 'John Doe', 'country': 'USA', 'field_of_interest': 'AI', 'budget': 'Medium'},
            {'name': 'Jane Smith', 'country': 'Canada', 'field_of_interest': 'Data Science', 'budget': 'High'},
            {'name': 'Ananda', 'country': 'India', 'field_of_interest': 'Business', 'budget': 'Low'},
            # Add more student profiles as needed
        ]
        self.universities = [
            'Harvard University', 'Stanford University', 'MIT', 'Oxford University', 'Cambridge University'
        ]
    
    def get_possible_actions(self):
        # Assuming each action corresponds to recommending a university
        return list(range(len(self.universities)))

    def reset(self):
        # Resets the environment to a random student profile
        return random.choice(self.students)

    def step(self, action):
        # Assuming that the action is recommending a university
        reward = random.choice([1, 0])  # Random reward (this should be based on actual logic)
        done = True  # End of step (for simplicity)
        next_state = random.choice(self.students)  # Transition to next random student profile
        return next_state, reward, done

class QAgent:
    def __init__(self, env):
        self.env = env
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.9  # Exploration rate
        self.q_table = np.zeros((len(self.env.students), len(self.env.universities)))  # Q-table initialized to zero
    
    def choose_action(self, state_index):
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < self.epsilon:
            # Exploration: choose a random university
            action = random.choice(self.env.get_possible_actions())
        else:
            # Exploitation: choose the best university based on Q-values
            action = np.argmax(self.q_table[state_index])
        return action

    def update_q_value(self, state_index, action, reward, next_state_index):
        current_q = self.q_table[state_index, action]
        max_future_q = np.max(self.q_table[next_state_index])  # Get the max Q value for the next state
        self.q_table[state_index, action] = current_q + self.alpha * (reward + self.gamma * max_future_q - current_q)

    def train(self, episodes=1000):
        """
        Train the Q-agent through multiple episodes without printing progress.
        """
        for episode in range(episodes):
            state = self.env.reset()  # Initial student state
            done = False
            while not done:
                state_index = self.env.students.index(state)  # Convert student to index
                action = self.choose_action(state_index)

                next_state, reward, done = self.env.step(action)

                next_state_index = self.env.students.index(next_state)  # Get the next state index
                self.update_q_value(state_index, action, reward, next_state_index)

                state = next_state

            # Decay epsilon (Exploration -> Exploitation)
            self.epsilon = max(0.1, self.epsilon * 0.995)  # Decay epsilon after each episode

            # Debugging: Print Q-values for each student profile
            if episode % 100 == 0:  # Print every 100 episodes
                print(f"Q-values after episode {episode}:")
                for i, student in enumerate(self.env.students):
                    print(f"Student: {student['name']}, Q-values: {self.q_table[i]}")

    def test(self, student_profile):
        state_index = self.env.students.index(student_profile)  # Convert student to index
        action = self.choose_action(state_index)  # Choose the action with highest Q-value
        recommended_university = self.env.universities[action]
        return recommended_university

if __name__ == "__main__":
    print("Welcome to the University Recommendation System!\n")
    print("This program will recommend a university based on a student's profile.\n")
    print("The following fields of interest are available:")
    print("- AI")
    print("- Data Science")
    print("- Business")
    print("- Engineering")
    print("- Arts\n")

    print("Available budgets:")
    print("- Low")
    print("- Medium")
    print("- High\n")

    print("To get a recommendation, please provide the following details:")
    print("Student Name, Country, Field of Interest (choose from AI, Data Science, Business, Engineering, Arts), Budget (choose one: Low, Medium, High)\n")

    # Initialize the environment and agent
    env = StudentAdvisorEnv()
    agent = QAgent(env)

    # Start training the agent (this will take a while)
    print("Training the agent... This will take a while, but no progress will be printed.")
    agent.train(1000)  # Train for 1000 episodes

    # Test the agent after training
    student_name = input("Enter Student Name: ")
    country = input("Enter Country: ")
    field_of_interest = input("Enter Field of Interest (choose from AI, Data Science, Business, Engineering, Arts): ")
    budget = input("Enter Budget (choose from Low, Medium, High): ")

    student_profile = {
        'name': student_name,
        'country': country,
        'field_of_interest': field_of_interest,
        'budget': budget
    }

    # Get a recommendation
    recommended_university = agent.test(student_profile)
    print(f"\nRecommended university for {student_name} is: {recommended_university}")
