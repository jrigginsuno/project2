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
        try:
            self.frame.num_attempts.trace_add('write', self.show_attempts)
        except ValueError as e:
            print('user value error')
        except TypeError:
            print('Type Error')

    def show_attempts(self, *args):
        # print(self.frame.num_attempts.get())
        try:
            self.clear_result()
            self.entry.set_attempt_count(self.frame.num_attempts.get())
            # print(len(self.frame.label_scores))
            for _ in range(self.entry.get_attempt_count()):
                self.frame.label_scores[_].grid(column=0, row=_ + 2)
                self.frame.entry_scores[_].grid(column=1, row=_ + 2)

        except ValueError as e:
            self.clear_attempts()
            self.show_result('Number of attempts is invalid', 1)
            # print(f'Error = {e}')
        except TypeError:
            print('Type Error')

    def clear_attempts(self):
        for _ in range(4):
            self.frame.label_scores[_].grid_forget()
            self.frame.entry_scores[_].grid_forget()

    def show_result(self, message, is_error):
        self.frame.label_result.grid(columnspan=2, row=7)
        if is_error:
            self.frame.label_result.grid()
            self.frame.label_result.config(fg='red')
        else:
            self.frame.label_result.config(fg='green')
        self.frame.label_result.config(text=message)

    def clear_result(self):
        self.frame.label_result.config(fg='red')
        self.frame.label_result.grid_forget()

    def submit_score(self):
        try:
            for _ in range(self.entry.get_attempt_count()):
                self.entry.set_score_value(self.frame.entry_scores[_].get(), _)
        except ValueError:
            self.show_result('Value of Scores must be between 0 and 100', 1)


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
            self.label_scores.append(tk.Label(self, text=f'Score {_+1}:'))
            self.entry_scores.append(tk.Entry(self))
            self.label_scores[_].grid(column=0, row=_+2)
            self.entry_scores[_].grid(column=1, row=_+2)

            self.label_scores[_].grid_forget()
            self.entry_scores[_].grid_forget()

        self.button_submit = tk.Button(self, text='Submit', command=lambda: self.controller.submit_score())
        self.button_submit.grid(columnspan=2, row=6)

        self.label_result = tk.Label(self, fg='red')
        self.label_result.grid(columnspan=2, row=7)
        self.label_result.grid_forget()



class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
