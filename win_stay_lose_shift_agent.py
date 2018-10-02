from agent import Agent

class WinStayLoseShiftAgent(Agent):
    def __init__(self, player_type):
        super(TitfortatAgent, self).__init__(player_type)
        self.prefer_defect = False
    
    def move(self):
        return self.prefer_defect

    def record_history(self, row_action, col_action, row_payoff, col_payoff):
        payoff = row_payoff if self.player_type == 0 else col_payoff
        if payoff < 3:
            self.prefer_defect = not self.prefer_defect