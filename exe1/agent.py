from thing import Thing

class Agent(Thing):
    def __init__(self, program=None):
        self.alive = True
        self.bump = False
        self.holding = []
        self.performance = 0
        # Use callable() for a more robust check
        if program is None or not callable(program):
            def program(percept):
                # This is the default interactive program if no valid program is provided
                return eval(input('Percept={}; action? '.format(percept)))
        self.program = program

    def can_grab(self, thing):
        return False