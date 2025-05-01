class func:
    def __init__(self, equation: str) -> None:
        """
        Initializes a func instance with the provided equation.

        Parameters:
        equation (str): Right side of f(x) = equation
        """

        self.equation = equation
        return
    
    def __call__(self, value: float) -> float:
        return eval(self.unsimplified_equation(value))
    
    def list_terms(self, start, num):
        return [self[i] for i in range(start, start + num)]
    
    def unsimplified_equation(self, index):
        return self.equation.replace("x", str(index))