class formula:
    def __init__(self, equation: str) -> None:
        self.equation = equation
        return
    
    def replace_vars(self, variables):
        equation = self.equation
        for key, value in variables.items():
            equation = equation.replace(key, str(value))
        return equation
    
    def calculate(self, **kwargs):
        return eval(self.replace_vars(kwargs))