from exe1.Agent import Agent

class myAgent(Agent):

    def __init__(self, program=None):
        super().__init__(program)
    
    def program(self, percept):
        if percept == "Thirty":
            return "Clean"
        return "Move"