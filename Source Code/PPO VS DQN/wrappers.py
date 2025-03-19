# This code is not our own. It was first used by the source below. 
# https://github.com/Sourish07/Super-Mario-Bros-RL/blob/main/agent.py
# Aryan Miriyala and Cedric Dortch

import numpy as np
from gym import Wrapper
from gym.wrappers import GrayScaleObservation, ResizeObservation, FrameStack

# This file has all of the wrappers that we want to use.

class SkipFrame(Wrapper):
    def __init__(self, env, skip):
        super().__init__(env)
        self.skip = skip
    
    def step(self, action):
        total_reward = 0.0
        done = False
        for _ in range(self.skip):
            next_state, reward, done, trunc, info = self.env.step(action)
            total_reward += reward
            if done:
                break
        return next_state, total_reward, done, trunc, info
    
# Applying and defining wrappers. Wrappers are explained in readme. 
def apply_wrappers(env):
    env = SkipFrame(env, skip=4) # Num of frames to apply one action to
    env = ResizeObservation(env, shape=84) # Resize frame from 240x256 to 84x84
    env = GrayScaleObservation(env)
    env = FrameStack(env, num_stack=4, lz4_compress=True) # May need to change lz4_compress to False if issues arise
    return env
