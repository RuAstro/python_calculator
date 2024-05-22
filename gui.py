import tkinter as tk
from main import *
from main import Calculator


class CalculatorGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")

        self.calc = Calculator()

        self.input_var = tk.StringVar()
        self.input_var.set("")

        self.create_widgets()
