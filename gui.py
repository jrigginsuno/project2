import tkinter as tk
from grader import Grader


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry = Grader()

        self.container = tk.Frame(self)
        self.container.pack()
        self.__create_widgets()

        self.handle_user_input()

    def __create_widgets(self):
        self.frame = InputFrame(self.container, self)
        self.frame.pack(pady=10)

    def handle_user_input(self):
        # try:
        self.frame.num_attempts.trace_add('write', self.show_attempts)
        # except:
        #     pass

    def show_attempts(self, *args):
        print(self.frame.num_attempts.get())
        self.entry.set_attempt()


# class MainFrame(tk.Frame):
# 	def __init__(self, parent, controller):
# 		super().__init__(parent)


class InputFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.label_student = tk.Label(self, text='Student name:')
        self.entry_student = tk.Entry(self)
        self.label_student.grid(column=0, row=0)
        self.entry_student.grid(column=1, row=0)

        self.num_attempts = tk.StringVar()
        self.num_attempts.set('')

        self.label_attempts = tk.Label(self, text='No. of attempts:')
        self.entry_attempts = tk.Entry(self, textvariable=self.num_attempts)
        self.label_attempts.grid(column=0, row=1)
        self.entry_attempts.grid(column=1, row=1)

        self.label_scores = []
        self.entry_scores = []
        for _ in range(4):
            self.label_scores.append(tk.Label(self, text=f'Score {_}:'))
            self.entry_scores.append(tk.Entry(self))
            self.label_scores[_].grid(column=0, row=_+2)
            self.entry_scores[_].grid(column=1, row=_+2)

            # self.label_scores[_].grid_forget()
            # self.entry_scores[_].grid_forget()

        self.button_submit = tk.Button(self, text='Submit')
        self.button_submit.grid(columnspan=2, row=6)


class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)