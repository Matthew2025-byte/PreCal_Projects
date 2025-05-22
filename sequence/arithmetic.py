class arithmetic_sequence:
    def __init__(self, start_value, difference):
        self.difference = difference
        self.start = start_value

    def __getitem__(self, index):
        return self.start + (index - 1) * self.difference
    
    @staticmethod
    def find_start(index, value, difference):
        return (index - 1) * difference - value
    
    @staticmethod
    def find_difference(start, entry: tuple) -> float:
        """entry: (index, value)"""
        return (entry[0] - start) / (entry[1] - 1)
    
class arithmetic_series:
    def __init__(self) -> None:
        return
    
    @staticmethod
    def sum(start_value, endvalue:tuple):
        """endvalue is tuple of (index, value)"""
        return (endvalue[0] / 2) * (start_value + endvalue[1])