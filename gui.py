import tkinter as tk
from main import *
from main import Calculator
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class CalculatorGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Calculator")

        self.calc = Calculator()

        self.input_var = tk.StringVar()
        self.input_var.set("")

        self.create_widgets()

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        log.info(f"Initialize {__class__.__name__}")

    def create_widgets(self):
        log.info("Creating widgets...")
        input_frame = tk.Frame(self.window)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.input_entry = tk.Entry(
            input_frame,
            textvariable=self.input_var,
            font=("", 14),
            bd=10,
            justify="left",
        )
        self.input_entry.pack(fill="x", expand=True)

        self.window.bind("<Return>", lambda event: self.calculate())

        button_frame = tk.Frame(self.window)
        button_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        buttons = [
            ("7", lambda: self.append_to_input("7"), "white", "black"),
            ("8", lambda: self.append_to_input("8"), "white", "black"),
            ("9", lambda: self.append_to_input("9"), "white", "black"),
            ("/ ", lambda: self.append_to_input("/"), "orange", "black"),
            ("4", lambda: self.append_to_input("4"), "white", "black"),
            ("5", lambda: self.append_to_input("5"), "white", "black"),
            ("6", lambda: self.append_to_input("6"), "white", "black"),
            ("x", lambda: self.append_to_input("*"), "orange", "black"),
            ("1", lambda: self.append_to_input("1"), "white", "black"),
            ("2", lambda: self.append_to_input("2"), "white", "black"),
            ("3", lambda: self.append_to_input("3"), "white", "black"),
            ("- ", lambda: self.append_to_input("-"), "orange", "black"),
            ("0", lambda: self.append_to_input("0"), "white", "black"),
            ("(", self.open_bracket, "blue", "black"),
            (")", self.close_bracket, "blue", "black"),
            ("+", lambda: self.append_to_input("+"), "orange", "black"),
            ("C", self.clear_input, "grey", "black"),
            ("% ", lambda: self.append_to_input("/100"), "grey", "black"),
            ("^", lambda: self.append_to_input("**"), "grey", "black"),
            ("=", self.calculate, "orange", "black"),
        ]

        for text, command, bg_color, fg_color in buttons:
            button = tk.Button(
                button_frame,
                text=text,
                font=("", 10),
                padx=5,
                pady=5,
                command=command,
                bg=bg_color,
                fg=fg_color,
            )
            button.grid(
                row=(buttons.index((text, command, bg_color, fg_color)) // 4),
                column=(buttons.index((text, command, bg_color, fg_color)) % 4),
                padx=5,
                pady=5,
                sticky="nsew",
            )

        # resize buttons to the size of user expand
        for i in range(4):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

    def append_to_input(self, value):
        current_input = self.input_var.get()
        self.input_var.set(current_input + value)
        log.info(f"Appended {value} to input")

    def open_bracket(self):
        current_input = self.input_var.get()
        self.input_var.set(current_input + "(")
        log.info("Added open bracket")

    def close_bracket(self):
        current_input = self.input_var.get()
        self.input_var.set(current_input + ")")
        log.info("Added close bracket")

    def clear_input(self):
        self.input_var.set("")
        log.info("Cleared input")

    def calculate(self):
        expression = self.input_var.get()
        expression = expression.replace("%", "/100")
        log.info(f"Calculating expression: {expression}")
        try:
            result = eval(expression)
            self.input_var.set(str(result))
            log.info(f"Result: {result}")
        except Exception as e:
            self.input_var.set("Error: need more sense")
            log.error(f"Error occurred during calculation: {e}")


if __name__ == "__main__":
    window = tk.Tk()
    app = CalculatorGUI(window)
    window.mainloop()
