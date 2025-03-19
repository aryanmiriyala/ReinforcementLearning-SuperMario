# This code is not our own, it was taken by the source below. 
# https://github.com/Sourish07/Super-Mario-Bros-RL/blob/main/agent_nn.py
# Aryan Miriyala and Cedric Dortch

import torch
from torch import nn
import numpy as np

# Used to teach artificial intelligence to process data. 
# This file is the neural network file with pytorch 

# Defining neural network class
# This is the class that defines the neural network that we will be working with and using for our algorithms
class AgentNN(nn.Module):
    def __init__(self, input_shape, n_actions, freeze=False):
        super().__init__()
        # Conolutional layers
        self.conv_layers = nn.Sequential(
            nn.Conv2d(input_shape[0], 32, kernel_size=8, stride=4),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=4, stride=2),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.ReLU(),
        )

        conv_out_size = self._get_conv_out(input_shape)

        # Linear layers
        self.network = nn.Sequential(
            self.conv_layers,
            nn.Flatten(),
            nn.Linear(conv_out_size, 512),
            nn.ReLU(),
            nn.Linear(512, n_actions)
        )

        # Freezes the agent and the game
        if freeze:
            self._freeze()
        
        # If we are using GPU, then use CUDA or just use CPU
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.to(self.device)

    def forward(self, x):
        return self.network(x)

    def _get_conv_out(self, shape):
        o = self.conv_layers(torch.zeros(1, *shape))
        # np.prod returns the product of array elements over a given axis
        return int(np.prod(o.size()))
    
    def _freeze(self):        
        for p in self.network.parameters():
            p.requires_grad = False