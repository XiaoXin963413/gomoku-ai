import gomoku_ai.base as base

class gomokuAI(base.BaseBoard):
    def Next_step(self):
        if self.check_five():
            return "Game over."
        if self.check_check():
            return "Next step win!"
        else:
            return "None!"