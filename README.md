# 🎓 Student Advisor Reinforcement Learning

An **AI-powered student academic advisor** built using **Reinforcement Learning (RL)**. The system learns to recommend optimal academic pathways, course selections, and universities based on student profiles and goals.

## 📌 Overview

This project applies Q-learning and custom reward shaping to create an intelligent student advisor agent. The agent interacts with a simulated academic environment, learning which recommendations maximize long-term student success outcomes.

## 📁 Project Structure

```
student_advisor_rl/
├── train.py                  # Main training script for the RL agent
├── agent.py                  # Q-learning agent implementation
├── q_agent.py                # Extended Q-agent with advanced features
├── environment.py            # Core RL environment definition
├── advisor_env.py            # Student advisor specific environment
├── reward_gpt.py             # GPT-assisted reward function
├── data.py                   # Data loading and preprocessing
├── test.py                   # Agent evaluation and testing
├── test_env.py               # Environment unit tests
├── students_data.json        # Student profile dataset
├── universities_data.json    # University information dataset
├── university_dataset.csv    # Structured university data
├── requirements.txt          # Python dependencies
└── venv/                     # Python virtual environment
```

## 🚀 Features

- **Custom RL Environment** — Gym-style academic advising environment
- **Q-Learning Agent** — Tabular Q-learning with epsilon-greedy exploration
- **GPT Reward Shaping** — Uses LLM to provide intelligent reward signals
- **Student Profiles** — Rich student data with grades, interests, goals
- **University Matching** — Recommends best-fit universities and programs
- **Training Visualization** — Reward curves and performance metrics

## 🛠️ Tech Stack

- **Python** — Core language
- **NumPy / Pandas** — Data processing
- **OpenAI API** — GPT-assisted reward computation
- **Matplotlib** — Training visualization
- **JSON** — Dataset storage

## 🏃 Getting Started

```bash
# Clone the repository
git clone https://github.com/1avishek/student-advisor-rl.git
cd student-advisor-rl

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Train the agent
python train.py

# Test the trained agent
python test.py
```

## 🧠 How It Works

1. **Environment**: Simulates student-advisor interactions over an academic session
2. **State Space**: Student GPA, interests, financial situation, target universities
3. **Action Space**: Academic recommendations (courses, universities, study plans)
4. **Reward**: Computed based on student outcome metrics + optional GPT feedback
5. **Agent**: Q-learning updates policy to maximize cumulative reward

## 📊 Training

The agent trains over multiple episodes, gradually improving its recommendation strategy through trial and error. Training curves show reward improvements over time.

## 📄 License

MIT License
