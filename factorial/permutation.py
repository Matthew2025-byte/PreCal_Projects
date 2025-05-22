from factorial import factorial
class permutation:
    def __init__(self, n, r) -> float:
        return factorial(n) / (factorial(n) - (factorial(r)))