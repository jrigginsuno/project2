import tkinter as tk


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.container = tk.Frame(self)
        self.container.pack()

        self.__create_widgets()

    def __create_widgets(self):
        self.frame = InputPage(self.container, self)
        self.frame.pack(pady=10)


# class MainFrame(tk.Frame):
# 	def __init__(self, parent, controller):
# 		super().__init__(parent)


class InputPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.label_student = tk.Label(self, text='Student name:')
        self.entry_student = tk.Entry(self, width=30)
        self.label_attempts = tk.Label(self, text='No. of attempts:')
        self.entry_attempts = tk.Entry(self, width=30)
        # self.button_add_student = tk.Button(self,
        #                                     text='Add Student',
        #                                     command=lambda: None )

        self.label_student.pack(padx=10)
        self.entry_student.pack(padx=10)
        self.label_attempts.pack(padx=10)
        self.entry_attempts.pack(padx=10)
        # self.button_add_student.pack(side='bottom')


class ResultPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
