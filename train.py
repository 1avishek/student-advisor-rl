import random
import pickle

class StudentAdvisorEnv:
    def __init__(self, student_data, university_data):
        self.student_data = student_data
        self.university_data = university_data

    def get_reward(self, student, university):
        reward = 0
        
        # Reward for matching the student's field with the university's field of excellence
        if student["field"] == university["field_of_excellence"]:
            reward += 10

        # Reward for budget compatibility
        if student["budget"] >= university["tuition_fee"]:
            reward += 5

        # Reward for location preference (if student prefers specific countries)
        if student["preferred_country"] == university["country"]:
            reward += 3
        
        # Add a penalty if the university's tuition is too high for the student's budget
        if student["budget"] < university["tuition_fee"]:
            reward -= 5  # Penalty for recommending an unaffordable university

        # Reward for university's reputation in the student's field
        if university["field_of_excellence"] == student["field"]:
            reward += university["reputation_score"]

        return reward


class StudentAdvisor:
    def __init__(self, students, universities, exploration_rate=0.9, exploration_decay=0.99):
        self.students = students
        self.universities = universities
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay
        self.env = StudentAdvisorEnv(students, universities)
        self.q_table = {}  # Initialize the Q-table for storing rewards
        self.student_to_index = {student['name']: index for index, student in enumerate(self.students)}

    def train(self, episodes=1000):
        for episode in range(1, episodes + 1):
            # Randomly select a student
            student = random.choice(self.students)
            student_index = self.student_to_index[student['name']]
            # Select a university either randomly or based on the exploration rate
            if random.random() < self.exploration_rate:
                university = random.choice(self.universities)  # Exploration
            else:
                university = self._select_best_university(student)  # Exploitation

            # Get the reward for recommending the university to the student
            reward = self.env.get_reward(student, university)

            # Log the episode
            print(f"🎓 Episode {episode}")
            print(f"Student: {student['name']}, Field: {student['field']}, Budget: {student['budget']}")
            print(f"Recommended University: {university['name']} in {university['country']}")
            print(f"Reward: {reward}\n")

            # Store reward in Q-table (simplified version for now)
            self.q_table[student_index] = {university['name']: reward}

            # Decay the exploration rate
            self.exploration_rate *= self.exploration_decay

    def _select_best_university(self, student):
        best_university = None
        best_reward = -float('inf')
        for university in self.universities:
            reward = self.env.get_reward(student, university)
            if reward > best_reward:
                best_reward = reward
                best_university = university
        return best_university

    def recommend_university(self, student_input):
        # Find the student from input
        student = {
            "name": student_input["name"],
            "field": student_input["field"],
            "budget": student_input["budget"],
            "preferred_country": student_input["preferred_country"]
        }
        
        # Select best university for the student based on the trained model
        recommended_university = self._select_best_university(student)
        return recommended_university


# Sample university data
universities = [
    {"name": "University of Helsinki", "country": "Finland", "field_of_excellence": "Medicine", "tuition_fee": 10000, "reputation_score": 8},
    {"name": "USA University of Science", "country": "USA", "field_of_excellence": "Engineering", "tuition_fee": 15000, "reputation_score": 7},
    {"name": "Canada University of Technology", "country": "Canada", "field_of_excellence": "Computer Science", "tuition_fee": 20000, "reputation_score": 9},
    {"name": "Germany University of Arts", "country": "Germany", "field_of_excellence": "Arts", "tuition_fee": 12000, "reputation_score": 6},
    {"name": "Australia University of Technology", "country": "Australia", "field_of_excellence": "Engineering", "tuition_fee": 18000, "reputation_score": 7},
]

# Sample student data
students = [
    {"name": "Student_1", "field": "Medicine", "budget": 10000, "preferred_country": "Finland"},
    {"name": "Student_2", "field": "Engineering", "budget": 15000, "preferred_country": "USA"},
    {"name": "Student_3", "field": "Computer Science", "budget": 20000, "preferred_country": "Canada"},
    {"name": "Student_4", "field": "Arts", "budget": 12000, "preferred_country": "Germany"},
    {"name": "Student_5", "field": "Engineering", "budget": 18000, "preferred_country": "Australia"},
]

# Initialize the advisor with students and universities
advisor = StudentAdvisor(students, universities)
advisor.train(episodes=1000)

# Function to take input from a user and recommend a university
def get_student_input():
    print("Please enter your details to get a university recommendation:")
    name = input("Your name: ")
    field = input("Your field of study (e.g., Computer Science, Law, Medicine): ")
    budget = int(input("Your budget: "))
    preferred_country = input("Preferred country (e.g., USA, Finland, Canada): ")

    student_input = {
        "name": name,
        "field": field,
        "budget": budget,
        "preferred_country": preferred_country
    }

    return student_input

# Take input from the user and recommend a university
student_input = get_student_input()
recommended_university = advisor.recommend_university(student_input)

print("\nRecommended University:")
print(f"University: {recommended_university['name']} in {recommended_university['country']}")
print(f"Field of Excellence: {recommended_university['field_of_excellence']}")
print(f"Tuition Fee: {recommended_university['tuition_fee']}")
