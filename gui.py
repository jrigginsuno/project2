import tkinter as tk
from grader import Student


class Gui(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.student = Student()

        self.container = tk.Frame(self)
        self.container.pack()
        self.__create_widgets()

    def __create_widgets(self) -> None:
        self.frame = InputFrame(self.container, self)
        self.frame.pack(pady=10)

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

    def submit(self) -> None:
        try:
            self.student.set_name(self.frame.entry_student.get())
            self.student.set_scores(list(map(lambda x: int(x.get()),
                                             self.frame.entry_scores[:self.frame.get_attempts()])))
            self.student.enter_grade()
            self.student.clear()
        except ValueError as e:
            self.show_result(e)
        else:
            self.frame.clear_entries()
            self.show_result()


class InputFrame(tk.Frame):
    def __init__(self, parent, controller) -> None:
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

        self.label_scores: list[tk.Label] = []
        self.entry_scores: list[tk.Entry] = []
        for i in range(4):
            self.label_scores.append(tk.Label(self, text=f'Score {i+1}:'))
            self.entry_scores.append(tk.Entry(self))

            self.label_scores[i].grid(column=0, row=i+2)
            self.entry_scores[i].grid(column=1, row=i+2)

            self.label_scores[i].grid_remove()
            self.entry_scores[i].grid_remove()

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

    def get_scores(self) -> list[int]:
        """
        Method to get scores from entries and return that as a list.
        :return: List of integers of scores.
        """

        try:
            scores: list[int] = []
            for i in range(self.get_attempts()):
                scores.append(int(self.entry_scores[i].get()))
                if scores[i] < 0 or scores[i] > 100:
                    raise ValueError
            return scores
        except ValueError:
            raise ValueError('Attempts needs to be a number between 0 and 100')

    def clear_entries(self) -> None:
        """Method that clears all entry boxes"""
        self.__num_attempts.set('')
        self.entry_student.delete(0, 'end')
        for i in self.entry_scores:
            i.delete(0, 'end')
