# Aryan Miriyala
# This is a sample environment creation for the Mario Screen and UI. I tried to use OpenAI's gym to download the Mario emulators
# and utilized python to run the environment and control Mario's action.
# Here the agent is just taking random actions.

import gym
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

# Create the environment
env = gym_super_mario_bros.SuperMarioBrosEnv()

# Reset the environment
observation = env.reset()

# Interact with the environment
done = False
while not done:
    action = env.action_space.sample()  # Uses action from SIMPLE_MOVEMENT
    observation, reward, done, info = env.step(action)
    env.render()  # Render the game (optional)

# Close the environment
env.close()
