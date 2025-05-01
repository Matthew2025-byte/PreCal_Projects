class arithmatic_sequence:
    def __init__(self, equation):
        self.equation = equation
        return
    
    def __getitem__(self, index):
        return eval(self.equation.replace('n', str(index)))
    
    def list_terms(self, start, num):
        return [self[i] for i in range(start, start + num)]