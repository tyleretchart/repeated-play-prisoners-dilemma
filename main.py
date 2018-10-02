import numpy as np

from game import Game
from random_agent import RandomAgent
from cooperate_agent import CooperateAgent
from oneshot_equilibrium_agent import OneshotEquilibriumAgent
from titfortat_agent import TitfortatAgent
from titfor2tat_agent import Titfor2tatAgent

#
# ======================================
# choose hyperparamters

TIMES_PLAYED = 1000
DISCOUNT_FACTOR = 0  # 0 means don't do it

#
# ======================================
# choose players

game = Game()
row_player = TitfortatAgent(game.ROW)
col_player = RandomAgent(game.COL)
game.register_players(row_player, col_player)

#
# ======================================
# play the game

row_scores = []
col_scores = []
if DISCOUNT_FACTOR > 0:
    play_again = True
    while play_again:
        game.tick()
        play_again = np.random.choice([True, False],
                                      p=[DISCOUNT_FACTOR, 1 - DISCOUNT_FACTOR])
else:
    for i in range(TIMES_PLAYED):
        game.tick()

print("|SUM| ROW: {}, COL: {}".format(
    np.sum(game.row_scores), np.sum(game.col_scores)))
print("|AVG| ROW: {}, COL: {}".format(
    np.mean(game.row_scores), np.mean(game.col_scores)))
