# PPO VS DQN 
Cedric Dortch 

## Description 
In this project I train the MARIO Agent to complete a level using the artificial intelligence algorithms PPO and DQN. My goal is to compare and contrast and see what the strengths and weaknesses are between both algorithms. 

## PPO Algorithm 

The PPO algorithm takes a small step size, so the agent can reach the optimal solution.
Combines A2C(multiple workers) and TRPO(It uses a trust region to improve the actor)
Resource Page: https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html
In the PPO.py file we are sending wrapped images to the PPO function so we can create the model. This is just the first test, further testing is required. For example, I may need to increase the learning rate since my computer does not have enough computational power to run large number of tests. I may need to change the n_steps variable as well.
Afterwards I test the model that I just created by passing the file into the PPO.load() function. Then I loop through the entire model.

## DQN Algorithm

Deep Q Network (DQN) builds on Fitted Q-Iteration (FQI) and make use of different tricks to stabilize the learning with neural networks: it uses a replay buffer, a target network and gradient clipping

Resource Page: https://stable-baselines3.readthedocs.io/en/master/modules/dqn.html
The DQN.py file is similar to the PPO.py file. But instead of using the PPO algorithm I am using the DQN algorithm. 

## Other Files
Wrappers.py is a file that contians the wrappers that we will use to wrap our environments and test the model. Here is a description of each wrapper used. 

Wrappers are a way we can modify our environments outputs. These are the wrappers that I use for my PPO and DQN algorithms

Skipframes Wrappers:
- Used to skip a numebr of frames in a environment. Helpful in accelerating training by reducing the number of frames processed. 

Resize Operation Wrappers 
- Used to resize the images in the environment. This can reduce computataional resoures. 

GreyScale Oberservation Wrappers 
- Converts colors to grayscale images. Reduces input dimensionality anc computational load. 

Framestack Wrappers 
- Framestack stacks frames together for a multi framed Oberservation. Allow algorithm to better capture information. 

DummyVecENV wrappers 
- Used to vectorize environments. Runs several copies of environment in parallel. 

## TESTING 
After running PPO.PY files and DQN.py I store the models into testing files. For PPO.py the files are train and logs. In DQN.py the files are logs2 and train2. The Logs and logs2 files can be anlysed in tensor board using the following command. 

cd logs
cd PPO_1
tensorboard --logdir=.

Running this command after going to the directory the log file is held in will give you a link. After copying the link to your browser you will be able to see information about your log file from your model. The information includes ep_len_mean, ep_rew_mean, entropy loss, learning rate, ect...

The train and train2 files hold the entire model that you ran. These are the models that will be kept for testing. 

## How to run?

Follow the requirements for installing gym. You also want to install stable_baselines3 from the websights above. 

# To intall

pip3 install -r requirements

# To run the sample environment, run this

python3 PPO.py
python3 DQN.py

# Resources: 
Helper files like wrappers.py are files created by someone else. References listed below! 

https://github.com/Sourish07/Super-Mario-Bros-RL/blob/main/README.md

https://github.com/nicknochnack/MarioRL

https://github.com/yfeng997/MadMario