class geometric_sequence:
    # formla: a_n = a_1 * r**(n - 1)
    def __init__(self, start_value, common_ratio) -> None:
        self.start = start_value
        self.ratio = common_ratio
        return
    
    def __getitem__(self, index):
        return self.start * self.ratio ** (index - 1)



class geometric_series:
    def __init__(self) -> None:
        pass

    @staticmethod
    def find_finite(**kwargs): # Too Complicated
        """use a_1, r, and n
        \nor use an a_n=[], starting with a_1
        """
        if 'a_1' in kwargs and 'r' in kwargs and 'n' in kwargs:
            return (kwargs['a_1'] * (1 - kwargs['r'] ** kwargs['n'])) / (1 - kwargs['r'])
        else:
            ratio = kwargs['a_n'][1] / kwargs['a_n'][0]
            return (kwargs['a_n'][0] * (1 - ratio**len(kwargs['a_n']))) / (1 - ratio)
        
    @staticmethod
    def find_infinite(series: list[float]):
        ratio = series[1] / series[0]
        if ratio > 1:
            return None
        return series[0] / (1 - ratio)

