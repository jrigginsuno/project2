import os.path
import csv


class Student:
    """
    A class representing details for a Student object.
    """
    def __init__(self) -> None:
        """
        Method to set default values of a student object.
        """
        self.__name: str = ''
        self.__scores: list[int] = [0] * 4

        # Check if file.csv already exists
        self.__file_exists: bool = os.path.isfile('file.csv')

    def get_name(self) -> str:
        """
        Method to access student's name.
        :return: Student's name.
        """
        return self.__name

    def set_name(self, name: str) -> None:
        """
        Method to access student's name.
        :param name: New name.
        """
        if name:
            self.__name = name
        else:
            raise ValueError('Name is empty')

    def get_scores(self) -> list[int]:
        """
        Method to access student's scores.
        :return: Student's scores.
        """
        return self.__scores

    def set_scores(self, scores: list[str | int]) -> None:
        """
        Method to modify a student's score.
        :param scores: New scores.
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
        """
        Method to set variables back to default values.
        """
        self.__name = ''
        self.__scores = [0] * 4

    def enter_grade(self) -> None:
        """
        Method to write values of a student into list and writes that as a row in a csv file.
        """
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
