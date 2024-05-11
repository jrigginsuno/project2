from typing import List


class Student:
    def __init__(self) -> None:
        """
        Method to set default values
        """
        self.__name: str = ''
        self.__attempts: int = 0
        # self.__scores: List[int] = [0, 0, 0, 0]
        self.__scores: List[int] = []

    @staticmethod
    def check_number(num: int) -> None:
        if num < 0:
            raise ValueError('Negative')

    def check_score(self, score: int) -> None:
        self.check_number(score)
        if score > 100:
            raise ValueError('Out of score range')

    def set_score_value(self, score_str: str, index: int) -> None:
        """
        Sets the value of an element in the score list
        :param score_str: String that is cast to int
        :param index: Index of list for where score is being written to
        :return:
        """

        score: int = int(score_str)
        self.check_score(score)
        self.__scores[index] = score
        # print(score)

    def get_name(self) -> str:
        """Getter method for name."""
        return self.__name

    def set_name(self, name: str) -> None:
        """Setter method for name."""
        if name:
            self.__name = name
        else:
            raise ValueError('Name is empty')

    def clear(self):
        self.__name = ''
        self.__attempts = 0
        for _ in range(len(self.__scores)):
            self.__scores[_] = 0
