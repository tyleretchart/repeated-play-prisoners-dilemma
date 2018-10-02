from agent import Agent

class DefectUnlessPunishedAgent(Agent):
    def __init__(self, player_type):
        super(TitfortatAgent, self).__init__(player_type)
        self.previous_action = 0
        self.punished = False
    
    def move(self):
        if not self.punished:
        	return 1
        else return self.previous_action 

    def record_history(self, row_action, col_action, row_payoff, col_payoff):
        if self.player_type == 0:
            self.previous_action = col_action
        else:
            self.previous_action = row_action