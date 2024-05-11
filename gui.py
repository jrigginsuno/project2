import tkinter as tk
from grader import Grader


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry = Grader()

        self.container = tk.Frame(self)
        self.container.pack()
        self.__create_widgets()

    def __create_widgets(self):
        self.frame = InputFrame(self.container, self)
        self.frame.pack(pady=10)

    def handle_user_input(self):
        try:
            # self.frame.num_attempts.trace_add('write', self.show_attempts)
            # self.frame.num_attempts.trace_add('write', self.show_attempts)
            pass
        except ValueError as e:
            print('user value error')
        except TypeError:
            print('Type Error')

    def show_result(self, error: Exception = None) -> None:
        """
        Method to show if given user inputs are valid.

        If this method is called with no argument no error will be displayed and will have green text
        If there is a given argument that exception will be displayed with red text.
        :param error: Value of an exception. Default is none
        :return:
        """

        if error:
            self.frame.label_result.config(fg='red', text=str(error))
        else:
            self.frame.label_result.config(fg='green', text='Submitted')
        self.frame.label_result.grid(columnspan=2, row=7)

    def clear_result(self):
        self.frame.label_result.config(fg='red')
        self.frame.label_result.grid_remove()

    def submit(self):
        # self.entry.set_name(self.frame.get_name())
        try:
            print(f'Name: {self.frame.get_name()}')
            print(f'Num Attempts: {self.frame.get_attempts()}')
            print(f'Scores: {self.frame.get_scores()}')
        except ValueError as e:
            self.show_result(e)
        else:
            self.frame.clear_entries()
            self.show_result()


class InputFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.__num_attempts: tk.StringVar = tk.StringVar()
        self.__num_attempts.trace_add('write', self.show_attempts)

        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.label_student = tk.Label(self, text='Student name:')
        self.entry_student: tk.Entry = tk.Entry(self)
        self.label_student.grid(column=0, row=0)
        self.entry_student.grid(column=1, row=0)

        self.label_attempts = tk.Label(self, text='No. of attempts:')
        self.entry_attempts = tk.Entry(self, textvariable=self.__num_attempts)

        self.label_attempts.grid(column=0, row=1)
        self.entry_attempts.grid(column=1, row=1)

        # self.label_scores = []
        self.label_scores: list[tk.Label] = []
        self.entry_scores: list[tk.Entry] = []
        for _ in range(4):
            self.label_scores.append(tk.Label(self, text=f'Score {_+1}:'))
            self.entry_scores.append(tk.Entry(self))

            self.label_scores[_].grid(column=0, row=_+2)
            self.entry_scores[_].grid(column=1, row=_+2)

            self.label_scores[_].grid_remove()
            self.entry_scores[_].grid_remove()

        self.button_submit = tk.Button(self, text='Submit', command=lambda: self.controller.submit())

        self.button_submit.grid(columnspan=2, row=6)

        self.label_result = tk.Label(self, fg='red')
        self.label_result.grid(columnspan=2, row=7)
        self.label_result.grid_remove()

    def get_attempts(self) -> int:
        """
        Returns the amount of attempts taken if given input is valid.

        :return: The amount of attempts taken.
        """

        try:
            num: int = int(self.__num_attempts.get())
            if num < 1 or num > 4:
                raise ValueError
        except ValueError:
            raise ValueError('Attempts needs to be a number between 1 and 4')
        else:
            return num

    def show_attempts(self, *args) -> None:
        """
        Dynamically adds label and entry to grid depending on the number of attempts given.
        If attempts are invalid all grid items are removed.

        :param args:
        :return:
        """

        try:
            for label, entry, _ in zip(self.label_scores, self.entry_scores, range(self.get_attempts())):
                label.grid()
                entry.grid()
        except ValueError:
            for label, entry in zip(self.label_scores, self.entry_scores):
                label.grid_remove()
                entry.grid_remove()

    def get_name(self) -> str:
        """
        Method to get the name of student from entry.
        :return: Name of student.
        """

        name: str = self.entry_student.get()
        if not name:
            raise ValueError('Name is empty')
        else:
            return name

    def get_scores(self) -> list[int]:
        """
        Method to get scores from entries and return that as a list.
        :return: List of integers of scores.
        """

        try:
            scores: list[int] = []
            for _ in range(self.get_attempts()):
                scores.append(int(self.entry_scores[_].get()))
                if scores[_] < 0 or scores[_] > 100:
                    raise ValueError
            return scores
        except ValueError:
            raise ValueError('Attempts needs to be a number between 0 and 100')

    def clear_entries(self) -> None:
        """
        Method that clears all entry boxes
        :return:
        """

        self.__num_attempts.set('')
        self.entry_student.delete(0, 'end')
        for _ in self.entry_scores:
            _.delete(0, 'end')


class ResultPage(tk.Frame):
    def __init__(self, parent, controller):

        super().__init__(parent)
