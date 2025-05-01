class arithmetic_sequence:
    def __init__(self, formula: str, **kwargs):
        self.kwargs = kwargs
        self.formula = formula
        return
    
    def __getitem__(self, index):
        return eval(self.unsimplified_equation(index))
    
    def list_terms(self, start, num):
        return [self[i] for i in range(start, start + num)]
    
    def unsimplified_equation(self, index):
        self.kwargs["n"] = index
        formula = self.formula
        for key, value in self.kwargs.items():
            try:
                formula = formula.replace(key, str(value))
            except:
                continue
        return formula
    




def sigma(start, end, formula) -> list:
    seq = arithmetic_sequence(formula)
    formulas = [seq.unsimplified_equation(i) for i in range(start, end + 1)]
    return eval("+".join(formulas))