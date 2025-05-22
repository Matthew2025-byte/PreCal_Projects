from factorial import factorial
class binomial:
    def __init__(self, n, r) -> float:
        return factorial(n) / (factorial(r) * (factorial(n) - (factorial(r))))