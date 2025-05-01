class arithmatic_sequence:
    def __init__(self, equation):
        self.equation = equation
        return
    
    def __getitem__(self, index):
        return eval(self.unsimplified_equation(index))
    
    def list_terms(self, start, num):
        return [self[i] for i in range(start, start + num)]
    
    def unsimplified_equation(self, index):
        return self.equation.replace('n', str(index))
    

def sigma(start, end, equation) -> list:
    seq = arithmatic_sequence(equation)
    equations = [seq.unsimplified_equation(i) for i in range(start, end + 1)]
    return eval("+".join(equations))