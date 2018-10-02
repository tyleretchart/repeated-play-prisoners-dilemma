import random
from agent import Agent


class RandomAgent(Agent):
    def move(self):
        return random.choice([0, 1])