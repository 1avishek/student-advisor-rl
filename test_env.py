# test_env.py

from environment import StudentAdvisorEnv

# Create the environment
env = StudentAdvisorEnv()

# Reset to get a new student
state = env.reset()
print("🎓 Student:")
print(state)

# Select the first university as a test action
action = 0
university, reward, done = env.step(action)

print("\n🏫 University Recommended:")
print(university)

print("\n💰 Reward (from GPT):")
print(reward)

print("\n✅ Done:", done)
