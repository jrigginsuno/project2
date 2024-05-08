from typing import List


class Grader:
    def __init__(self) -> None:
        """
        Method to set default values
        """
        self.__name: str = ''
        self.__attempts: int = 0
        self.__scores: List[int] = [0, 0, 0, 0]

    def is_valid_number(self):
        pass

    def is_valid_attempt(self, attempts: str):
        pass

    def is_valid_score(self):
        pass

    def set_attempt(self):
        pass

    def clear(self):
        pass

