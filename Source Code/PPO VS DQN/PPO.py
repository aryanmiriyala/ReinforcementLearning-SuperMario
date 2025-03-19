# Virtual environment is called m1.
# Activate your virtual environment before you start.
# Watch youtube video before you run your code.

# cd logs, cd PPO_39 , tensorboard --logdir=., Then copy the link.

# Cedric Dortch
# PPO Algorithm

# The PPO algorithm takes a small step size, so the agent can reach the optimal solution.
# Combines A2C(multiple workers) and TRPO(It uses a trust region to improve the actor) algorithms
# Inspired from Nicholas Renotte's PPO algorithm
# GitHub: https://github.com/nicknochnack/MarioRL/blob/
# main/Mario%20Tutorial.ipynb

from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3 import PPO
import gym_super_mario_bros
from gym_super_mario_bros.actions import RIGHT_ONLY
from nes_py.wrappers import JoypadSpace
from matplotlib import pyplot as plt
import os
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from stable_baselines3 import PPO
import numpy as np
from stable_baselines3.common.callbacks import BaseCallback

import torchvision
from wrappers import apply_wrappers
from agent import Agent

ENV_NAME = 'SuperMarioBros-1-1-v0'
# ENV_NAME = 'SuperMarioBros-v0'

# Change when you want to train the model
SHOULD_TRAIN = False
SHOULD_TEST = True
DISPLAY = True
# NUM_OF_EPISODES = 10  # Change the number of episodes

#********************************************************************************
# Saving the models Functions.

class TrainAndLoggingCallback(BaseCallback):

    def __init__(self, check_freq, save_path, verbose=1):
        super(TrainAndLoggingCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path

    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self):
        if self.n_calls % self.check_freq == 0:
            model_path = os.path.join(
                self.save_path, 'PPO_best_model_{}'.format(self.n_calls))
            self.model.save(model_path)

        return True

CHECKPOINT_DIR = './train/'
LOG_DIR = './logs/'
callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR)
#********************************************************************************

# Wrapping our environments
env = gym_super_mario_bros.make(
    ENV_NAME, render_mode='human' if DISPLAY else 'rgb_array', apply_api_compatibility=True)
env = JoypadSpace(env, RIGHT_ONLY)

env = apply_wrappers(env)
JoypadSpace.reset = lambda self, **kwargs: self.env.reset(**kwargs)

ppo_model = PPO('CnnPolicy', env, verbose=1,
                tensorboard_log=LOG_DIR, learning_rate=0.0001, n_steps=512) #Changing the learning rate. 

# Change to true or false when you want to train the model. 
if SHOULD_TRAIN:
    ppo_model.learn(total_timesteps=100000, callback=callback)

# Testing the models we created
#***************************************************************************
if SHOULD_TEST:
    model = PPO.load('./train/PPO_best_model_100000', env=env)  # This is good

    # Fix this error below!
    # state = env.reset()

    vec_env = model.get_env()
    obs = vec_env.reset()
    # Loop through the game
    while True:
        action, _ = model.predict(obs)
        action = [int(action)]  # Convert NumPy array to integer
        obs, reward, done, info = model.env.step(action)

    #    Convert LazyFrames object to numpy array
        obs = obs.__array__()

        model.env.render()

        if done:
            obs = model.env.reset()  # Reset the environment if done
#************************************************************************