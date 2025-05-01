class arithmetic_sequence:
    def __init__(self, equation: str, **kwargs):
        self.kwargs = kwargs
        self.equation = equation
        return
    
    def __getitem__(self, index):
        return eval(self.unsimplified_equation(index))
    
    def list_terms(self, start, num):
        return [self[i] for i in range(start, start + num)]
    
    def unsimplified_equation(self, index):
        self.kwargs["n"] = index
        equation = self.equation
        for key, value in self.kwargs.items():
            try:
                equation = equation.replace(key, str(value))
            except:
                continue
        return equation
    




def sigma(start, end, equation) -> list:
    seq = arithmetic_sequence(equation)
    equations = [seq.unsimplified_equation(i) for i in range(start, end + 1)]
    return eval("+".join(equations))