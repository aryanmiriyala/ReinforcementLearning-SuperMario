# Aryan Miriyala and Cedric Dortch
## How to run the code readme

## The following steps need to be followed to run the game with the models that we have trained.

1. Clone the repository: Git clone: https://gitlab.com/amiriya/sp2024_cs4200_finalproject_g15.git

2. Before we start anything, we want to install the gym-super-mario-bros package. This will provide us with an emulator and screen to actually run the game. We are using the standard version, but with a few modifications to the code, you should be able to use any of the versions that OpenAI has available.

### To install super mario bros, run this command:
pip3 install gym-super-mario-bros

### Below is the link to the OpenAI Mario page for your reference:
https://pypi.org/project/gym-super-mario-bros/

3. Now, to run our game we will need to create a virtual environment with the given python configuration. To achieve this, run the following command.

### Running the following command will create a virtul environment with the required python configuration:
https://github.com/nicknochnack/MarioRL/blob/main/Mario%20Tutorial.ipynb

4. Once a virtual environment is created, activate it using anaconda. To do this, make sure you have anaconda installed on your machine.

### To install Anaconda, use go here and follow the instructions:
https://docs.anaconda.com/free/anaconda/install/index.html

### Once anaconda has been installed, you can use this command to activate your virtual environment:
conda activate smbrl

5. Next step is to install PyTorch. PyTorch installation in specific to specific machine, so it is recommended that you go to their website to follow what is needed and is local to your machine.

### This website contains information about PyTorch:
https://pytorch.org/get-started/locally/

### Or, you can use these commands and use pip3 to install them:
pip3 install torch
pip3 install torchvision
pip3 install torchaudio
pip3 install tensorboard

### If at all you run into any error later on when you try to run one of the algorithms, just reinstall these.

6. We will need stablebaselines which contain all the required reinforcement learning algorithms that we will be using.

## Follow this command to install stable baselines:
pip3 install stable-baselines3
pip3 install 'shimmy>=0.2.1'

## Alternatively, you could go on to their website and follow the commands to get the right version:
https://stable-baselines3.readthedocs.io/en/master/guide/install.html

7. Now, we need to install all the requirements that are needed to run the Mario environment.

### Follow and run this command to install all the necessary requirements:
pip3 install -r requirements.txt

8. Choose a file you want to run. (PPO.py or DQN.py) If this is the first time running set the SHOULD_TEST variable to False and the SHOULD_Train variable to True.
You are able to change the learning rate and the n_steps variable for testing purposes. (DQN does not have n_steps)
You can also change the total_timesteps variable: If you have a regular computer avoid setting the variable to a higher number, this will take too much time. 
Also be sure the timesteps is bigger than n_steps becuase if it is not your model will not be saved. 

9. After you run the file your model will be stored in the train or train2 file depending on which file you select.
And your logs will be stored in the logs or logs2 file. 
You can use tensor board to see how your training performed. 
### After you run the file use the following commands: 
cd logs
cd PPO_1
tensorboard --logdir=.
This is an example for the PPO file. In DQN the directory is called logs2 and the name of your logs will be DQN_1
These commands will give you a link, copy the link into web browser and you will be able to see the average reward, entropy loss, learning rate, and other parameters.

10. When you are done training and you want to test. Set SHOULD_TRAIN to False and SHOULD_TEST to True. 
locate the .load() function and change the file path to the correct path that holds the model you want to test. 
The model will be in train or train2 depending on which file you are running. 
Example: model = PPO.load('./train/PPO_best_model_10000', env=env)
Again, After you are done testing your model your model should be saved in the train file. 

### HAPPY TESTING! 