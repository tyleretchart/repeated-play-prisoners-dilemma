from agent import Agent

class PavlovAgent(Agent):
    def __init__(self, player_type):
        super(PavlovAgent, self).__init__(player_type)
        self.agree = True
    
    def move(self):
        return int(not self.agree)

    def record_history(self, row_action, col_action, row_payoff, col_payoff):
        self.agree = row_action == col_action

