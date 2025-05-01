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