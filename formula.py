class formula:
    def __init__(self, equation: str) -> None:
        self.equation = equation
        return
    
    def unsimplified_equation(self, value):
        return self.equation.replace("x", str(value))
    
    def calculate(self, value):
        return eval(self.unsimplified_equation(value))