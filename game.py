import numpy as np


class Game:
    def __init__(self):
        self.ROW = 0
        self.COL = 1
        self.payoff_matrix = np.array([[[3, 1], [5, 2]], [[3, 5], [1, 2]]])
        self.row_scores = []
        self.col_scores = []
        self.row_actions = []
        self.col_actions = []

    def register_players(self, row_player, col_player):
        self.row_player = row_player
        self.col_player = col_player

    def apply_move(self, row_player_action, col_player_action):
        row_player_payoff = self.payoff_matrix[
            self.ROW][row_player_action][col_player_action]
        col_player_payoff = self.payoff_matrix[
            self.COL][row_player_action][col_player_action]
        return row_player_payoff, col_player_payoff

    def tick(self):
        # make action
        row_action = self.row_player.move()
        col_action = self.col_player.move()
        # record action
        self.row_actions.append(row_action)
        self.col_actions.append(col_action)
        # apply action
        row_payoff, col_payoff = self.apply_move(row_action, col_action)
        # record results
        self.row_scores.append(row_payoff)
        self.col_scores.append(col_payoff)
        self.row_player.record_history(row_action, col_action, row_payoff,
                                       col_payoff)
        self.col_player.record_history(row_action, col_action, row_payoff,
                                       col_payoff)
