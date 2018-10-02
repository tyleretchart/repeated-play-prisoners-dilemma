class Agent:
    def __init__(self, player_type):
        self.player_type = player_type

    def move(self):
        raise NotImplementedError

    def record_history(self, row_action, col_action, row_payoff, col_payoff):
        pass