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

    def create_widgets(self):
        input_frame = tk.Frame(self.window)
        input_frame.pack(padx=10, pady=10)

        self.input_entry = tk.Entry(
            input_frame,
            textvariable=self.input_var,
            font=("", 14),
            bd=5,
            justify="right",
        )
        self.input_entry.pack(fill="x")

        button_frame = tk.Frame(self.window)
        button_frame.pack(padx=10, pady=10)

        buttons = [
            ("7", lambda: self.append_to_input("7")),
            ("8", lambda: self.append_to_input("8")),
            ("9", lambda: self.append_to_input("9")),
            ("+", lambda: self.append_to_input("+")),
            ("4", lambda: self.append_to_input("4")),
            ("5", lambda: self.append_to_input("5")),
            ("6", lambda: self.append_to_input("6")),
            ("-", lambda: self.append_to_input("-")),
            ("1", lambda: self.append_to_input("1")),
            ("2", lambda: self.append_to_input("2")),
            ("3", lambda: self.append_to_input("3")),
            ("*", lambda: self.append_to_input("*")),
            ("C", self.clear_input),
            ("0", lambda: self.append_to_input("0")),
            ("/", lambda: self.append_to_input("/")),
            ("=", self.calculate),
        ]

        for text, command in buttons:
            button = tk.Button(
                button_frame,
                text=text,
                font=("", 14),
                padx=10,
                pady=10,
                command=command,
            )
            button.grid(
                row=(buttons.index((text, command)) // 4),
                column=(buttons.index((text, command)) % 4),
            )

    def append_to_input(self, value):
        current_input = self.input_var.get()
        self.input_var.set(current_input + value)

    def clear_input(self):
        self.input_var.set("")

    def calculate(self):
        expression = self.input_var.get()
        try:
            result = eval(expression)
            self.input_var.set(str(result))
        except Exception as e:
            self.input_var.set("Error")
            print(e)


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorGUI(window)
    window.mainloop()
