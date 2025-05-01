class arithmetic_sequence:
    def __init__(self, difference, index, value):
        self.difference = difference
        self.start = (index - 1) * self.difference - value

    def __getitem__(self, index):
        return self.start + (index - 1) * self.difference