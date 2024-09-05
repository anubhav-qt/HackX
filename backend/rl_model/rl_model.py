import numpy as np

# Actions: Flashcards, Quiz, Video
ACTIONS = ['flashcards', 'quiz', 'video']

# Initialize Q-table
Q = np.zeros((3, len(ACTIONS)))  # 3 states (quiz score, time spent, improvement)

# Hyperparameters
alpha = 0.1   # Learning rate
gamma = 0.6   # Discount factor
epsilon = 0.1  # Exploration-exploitation trade-off

# Example: Simulate a user's response to a learning method (reward system)
def get_reward(action):
    if action == 'flashcards':
        return np.random.choice([1, 2, 3])  # Reward based on engagement
    elif action == 'quiz':
        return np.random.choice([0, 1, 2])  # Reward based on improvement in score
    elif action == 'video':
        return np.random.choice([1, 2])  # Reward based on time spent

# Simulate states (quiz score, time spent, improvement in performance)
def get_state():
    return np.random.choice([0, 1, 2])  # Simplified for demo (0=low, 1=medium, 2=high)

# Q-Learning algorithm
def train_q_learning(epochs=1000):
    for epoch in range(epochs):
        # Get initial state
        state = get_state()

        # Choose action (ε-greedy strategy)
        if np.random.uniform(0, 1) < epsilon:
            action_idx = np.random.choice(len(ACTIONS))  # Explore
        else:
            action_idx = np.argmax(Q[state])  # Exploit

        action = ACTIONS[action_idx]

        # Get reward based on action
        reward = get_reward(action)

        # Get new state
        new_state = get_state()

        # Q-learning update rule
        Q[state, action_idx] = Q[state, action_idx] + alpha * (reward + gamma * np.max(Q[new_state]) - Q[state, action_idx])

    return Q

# Train the model and save Q-values
Q_values = train_q_learning()
