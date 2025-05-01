class arithmetic_sequence:
    # Sum of an Arithmetic Series:
    # S_n = n/2 * (a_1 + a_n)
    def __init__(self, difference, index, value):
        self.difference = difference
        self.start = (index - 1) * self.difference - value

    def __getitem__(self, index):
        return self.start + (index - 1) * self.difference