import os.path
import csv


class Student:
    def __init__(self) -> None:
        """Method to set default values"""
        self.__name: str = ''
        self.__attempts: int = 0
        self.__scores: list[int] = [0] * 4

        # Check if file.csv already exists
        self.__file_exists: bool = os.path.isfile('file.csv')

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

    def set_scores(self, scores: list[str | int]) -> None:
        """
        Setter method for scores.

        Takes in list of strings and cast each element to int
        :param scores: List of strings to be converted to int and then stored to scores
        """

        try:
            scores = list(map(lambda x: int(x), scores))

            for i, val in enumerate(scores):
                if val < 0 or val > 100:
                    raise ValueError
                self.__scores[i] = val
        except ValueError:
            raise ValueError('Attempts needs to be a number between 0 and 100')

    def clear(self) -> None:
        """Set variables back to default values"""
        self.__name = ''
        self.__attempts = 0
        self.__scores = [0] * 4

    def enter_grade(self) -> None:
        with open('file.csv', 'a', newline='') as csvfile:
            content = csv.writer(csvfile)

            # Add header if file does not exist
            if not self.__file_exists:
                content.writerow(['Name', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Final'])
                self.__file_exists = True

            # Put all values into list for writing into csv file
            row: list = [self.__name]
            row.extend(self.__scores)
            row.append(max(self.__scores))

            content.writerow(row)
