from typing import List


class Student:
    def __init__(self) -> None:
        """Method to set default values"""
        self.__name: str = ''
        self.__attempts: int = 0
        self.__scores: list[int] = [0] * 4

    @staticmethod
    def check_number(num: int) -> None:
        if num < 0:
            raise ValueError('Negative')

    def get_name(self) -> str:
        """Getter method for name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Setter method for name."""
        if name:
            self.__name = name
        else:
            raise ValueError('Name is empty')

    def get_scores(self) -> list[int]:
        """Getter method for scores."""
        return self.__scores

    def set_scores(self, scores: list[str]) -> None:
        """Setter method for scores."""
        try:
            for i, val in enumerate(scores):
                val = int(val)
                if val < 0 or val > 100:
                    raise ValueError
                self.__scores[i] = val
        except ValueError:
            raise ValueError('Attempts needs to be a number between 0 and 100')

    # TODO
    def clear(self):
        self.__name = ''
        self.__attempts = 0
        for _ in range(len(self.__scores)):
            self.__scores[_] = 0
