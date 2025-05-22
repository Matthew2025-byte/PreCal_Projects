class factorial:
    def __init__(self, num:int) -> None:
        self.num = num
    def __str__(self) -> str:
        x:int = int(self.num)
        equation = ""
        while x > 0:
            equation += f"{x}*"
            x -= 1
        equation += "1"
        return str(eval(equation))