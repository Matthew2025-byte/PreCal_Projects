from .vector.vector2 import vec2
from .vector.vector3 import vec3
from .formula import formula
from .sequence.arithmetic import arithmetic_sequence, arithmetic_series
from .sequence.geometric import geometric_sequence, geometric_series

class sequence(formula):
    def __getitem__(self, index):
        return self.calculate(n=index)
class func(formula):
    def __call__(self, value):
        return self.calculate(value, x=value)