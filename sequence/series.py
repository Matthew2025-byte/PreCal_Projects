from __init__ import sequence
class series:
    def __init__(self, equation) -> None:
        self.equation = equation
        return
    
    def evaluate(self, start, end):
        return sum([sequence(self.equation)[i] for i in range(start, end + 1)])
    
    def __getitem__(self, index):
        return self.evaluate(1, index)
    
    def __call__(self, start, end):
        return self.evaluate(start, end)