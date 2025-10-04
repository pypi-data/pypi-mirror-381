class Example:
    def __init__(self, n: int):
        self.n = n


    def number_even(self) -> bool:
        if self.n % 2 == 0:
            return True
        else:
            return False