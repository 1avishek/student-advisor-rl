import random
from reward_gpt import mock_reward

class StudentAdvisorEnv:
    def __init__(self):
        self.students = [
            {"name": "John Doe", "country": "USA", "background": "CS", "interests": "AI", "budget": "High", "language": "English"},
            {"name": "Jane Smith", "country": "India", "background": "Engineering", "interests": "Robotics", "budget": "Medium", "language": "English"},
            # Add more students here...
        ]

        self.universities = [
            {"name": "Harvard University", "location": "USA", "programs": ["AI", "Robotics"], "tuition": 50000, "language": "English"},
            {"name": "Stanford University", "location": "USA", "programs": ["Computer Science"], "tuition": 45000, "language": "English"},
            # Add more universities here...
        ]

    def reset(self):
        # Randomly select a student from the list to start the simulation
        return random.choice(self.students)

    def step(self, action):
        """
        Perform a step in the environment: recommend a university and get a reward.
        
        Parameters:
            action (int): The index of the chosen university.
        
        Returns:
            tuple: The next student, the reward, and whether the episode is done.
        """
        student = random.choice(self.students)
        university = self.universities[action]
        
        # Get the reward for this student-university match
        reward = mock_reward(student, university)
        
        # For simplicity, assume the episode ends after one step
        done = True
        
        return university, reward, done

    def get_possible_actions(self):
        """
        Get all possible universities the agent can choose from.
        """
        return list(range(len(self.universities)))

# Example usage
if __name__ == "__main__":
    env = StudentAdvisorEnv()
    print("Initial state:", env.reset())
