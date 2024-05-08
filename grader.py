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
    def check_number(num: int) -> None:
        if num < 0:
            raise ValueError('Negative')

    def check_attempt_count(self, amount: int) -> None:
        self.check_number(amount)
        if amount < 1 or amount > 4:
            raise ValueError('Out of attempt range')

    def set_attempt_count(self, amount_str: str) -> None:
        # print(type(amount_str))
        amount: int = int(amount_str)
        self.check_attempt_count(amount)
        self.__attempts = amount
        # print(self.__attempts)

    def get_attempt_count(self) -> int:
        return self.__attempts

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

    def clear(self):
        pass
