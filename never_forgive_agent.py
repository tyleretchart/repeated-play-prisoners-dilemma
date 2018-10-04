from agent import Agent

class NeverForgiveAgent(Agent):
    def __init__(self, player_type):
        super(NeverForgiveAgent, self).__init__(player_type)
        self.punish = False
    
    def move(self):
        return int(self.punish)

    def record_history(self, row_action, col_action, row_payoff, col_payoff):
        if row_action == 1 or col_action == 1:
            self.punish = True
