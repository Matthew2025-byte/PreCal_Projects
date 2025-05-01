class arithmatic_sequence:
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
    
class arithmatic_series:
    # Sum of an Arithmetic Series:
    # S_n = n/2 * (a_1 + a_n)
    ...
class geometric_series:
    # Sum of a Geometric Series:
    # S_n = (a_1 * (1 - r^n)) / (1 - r)
    ...


def sigma(start, end, equation) -> list:
    seq = arithmatic_sequence(equation)
    equations = [seq.unsimplified_equation(i) for i in range(start, end + 1)]
    return eval("+".join(equations))