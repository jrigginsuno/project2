from typing import List


class Grader:
    def __init__(self) -> None:
        """
        Method to set default values
        """
        self.__name: str = ''
        self.__attempts: int = 0
        self.__scores: List[int] = [0, 0, 0, 0]

    @staticmethod
    def check_valid_number(num: int) -> None:
        if num <= 0:
            raise ValueError('Negative')

    def check_valid_attempt(self, amount: int) -> None:
        self.check_valid_number(amount)
        if amount > 4:
            raise ValueError('Out of attempt range')

    def is_valid_score(self):
        pass

    def set_attempt(self, amount_str: str) -> None:
        print(type(amount_str))
        amount: int = int(amount_str)
        self.check_valid_attempt(amount)
        self.__attempts = amount
        print(self.__attempts)

    def get_attempt(self) -> int:
        return self.__attempts

    def clear(self):
        pass
