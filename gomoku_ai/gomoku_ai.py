import gomoku_ai.base as base

class gomokuAI(base.BaseBoard):
    def __init__(self):
        super().__init__()
        
    def Next_step(self):
        state = "None"
        for x in range(len(self._board)):
            for y in range(len(self._board)):
                if self.check_five(x, y):
                    state = "Game over."
                    break
                if self.check_four(x, y):
                    state = "Next step win!" + str(self.check_four(x, y))
                    break
        return state