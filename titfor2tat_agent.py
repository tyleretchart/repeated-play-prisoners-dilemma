from agent import Agent

class Titfor2tatAgent(Agent):
    def __init__(self, player_type):
        super(Titfor2tatAgent, self).__init__(player_type)
        self.number_of_times_defected = 0
    
    def move(self):
        if self.number_of_times_defected > 1:
            return 1
        else:
            return 0

    def record_history(self, row_action, col_action, row_payoff, col_payoff):
        if self.player_type == 0:
            other_action = col_action
        else:
            other_action = row_action
            
        if other_action == 1:
            self.number_of_times_defected += 1
        else:
            self.number_of_times_defected = 0
