# This code is not our own. It was first used by the source below. 
# https://github.com/Sourish07/Super-Mario-Bros-RL/blob/main/agent.py
# Aryan Miriyala and Cedric Dortch

import time
import datetime

def get_current_date_time_string():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H_%M_%S")

#Defining Timer class
class Timer():
    def __init__(self):
        self.times = []

    def start(self):
        self.t = time.time()

    def print(self, msg=''):
        print(f"Time taken: {msg}", time.time() - self.t)

    def get(self):
        return time.time() - self.t
    
    def store(self):
        self.times.append(time.time() - self.t)

    def average(self):
        return sum(self.times) / len(self.times)