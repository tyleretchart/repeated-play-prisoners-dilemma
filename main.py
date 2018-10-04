import numpy as np

from game import Game
from random_agent import RandomAgent
from cooperate_agent import CooperateAgent
from oneshot_equilibrium_agent import OneshotEquilibriumAgent
from titfortat_agent import TitfortatAgent
from titfor2tat_agent import Titfor2tatAgent
from pavlov_agent import PavlovAgent
from never_forgive_agent import NeverForgiveAgent
from win_stay_lose_shift_agent import WinStayLoseShiftAgent
from exploit_forgiving_agent import ExploitForgivingAgent

import matplotlib.pyplot as plt

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




FINITE_DEFINITE = 0
DISCOUNT_FACTOR = []

row_agents = [OneshotEquilibriumAgent,
			  RandomAgent,
			  CooperateAgent,
			  TitfortatAgent,
			  Titfor2tatAgent,
			  PavlovAgent,
			  WinStayLoseShiftAgent,
			  NeverForgiveAgent,
			  ExploitForgivingAgent]


column_agents = [OneshotEquilibriumAgent,
				 RandomAgent,
				 CooperateAgent,
				 TitfortatAgent,
				 Titfor2tatAgent,
				 PavlovAgent,
				 WinStayLoseShiftAgent,
				 NeverForgiveAgent,
				 ExploitForgivingAgent]

results = np.zeros([6, len(row_agents), len(column_agents)])

fixed_lengths = [5, 100, 200]

for index, length in enumerate(fixed_lengths):
	for i, r in enumerate(row_agents):
		for j, c in enumerate(column_agents):
			game = Game()
			r_agent = r(game.ROW)
			c_agent = c(game.COL)
			game.register_players(r_agent, c_agent)
			for k in range(length):
				game.tick()
			results[index, i, j] = np.mean(game.row_scores)

heads_probabilities = [.75, .9, .99]

for index, p in enumerate(heads_probabilities):
	for i, r in enumerate(row_agents):
		for j, c in enumerate(column_agents):
			result = []
			for k in range(1000):
				game = Game()
				r_agent = r(game.ROW)
				c_agent = c(game.COL)
				game.register_players(r_agent, c_agent)
				while True:
					game.tick()
					if np.random.rand() > p:
						break
				result.append(np.mean(game.row_scores))

			results[index+3, i, j] = np.mean(result)

print(results)
print(np.mean(results, axis=1))

game_types=['5 Rounds', '100 Rounds', '200 Rounds', 'Beta = .75', 'Beta = .9', 'Beta = .99']

for i in range(results.shape[0]):

	# Set figure width to 12 and height to 9
	plt.rcParams["figure.figsize"] = [5, 5.3]

	plt.imshow(-results[i], interpolation='nearest', cmap='bwr')

	# Turn off tick labels
	plt.xticks([])
	plt.yticks([])

	# Row labels
	plt.text(-0.6, 0.3, r'AD', fontsize=12, ha='right')
	plt.text(-0.6, 1.3, r'Rand', fontsize=12, ha='right')
	plt.text(-0.6, 2.3, r'AC', fontsize=12, ha='right')
	plt.text(-0.6, 3.3, r'TfT', fontsize=12, ha='right')
	plt.text(-0.6, 4.3, r'Tf2T', fontsize=12, ha='right')
	plt.text(-0.6, 5.3, r'Pavlov', fontsize=12, ha='right')
	plt.text(-0.6, 6.3, r'WSLS', fontsize=12, ha='right')
	plt.text(-0.6, 7.3, r'NF', fontsize=12, ha='right')
	plt.text(-0.6, 8.3, r'Ours', fontsize=12, ha='right')

	# Column labels
	plt.text(0.3, 8.6, r'AD', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(1.3, 8.6, r'Rand', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(2.3, 8.6, r'AC', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(3.3, 8.6, r'TfT', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(4.3, 8.6, r'Tf2T', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(5.3, 8.6, r'Pavlov', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(6.3, 8.6, r'WSLS', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(7.3, 8.6, r'NF', fontsize=12, ha='right', va='top', rotation=-70)
	plt.text(8.3, 8.6, r'Ours', fontsize=12, ha='right', va='top', rotation=-70)

	plt.text(4, -1, r"Tournament Results ("+game_types[i]+")", fontsize=13, ha='center')
	plt.show()