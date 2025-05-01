class arithmetic_series:
    # Sum of an Arithmetic Series:
    # S_n = n/2 * (a_1 + a_n)
    def __init__(self, interval, index, value):
        self.interval = interval
        self.start = (index - 1) * self.interval - value

    def __getitem__(self, index):
        return self.start + (index - 1) * self.interval