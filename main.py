import logging

logging.basicConfig(level=logging.INFO)


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        #        logging.info(f"Added {num}. Result: {self.result}")
        return self.result

    def subtract(self, num):
        self.result -= num
        #        logging.info(f"Subtracted {num}. Result: {self.result}")
        return self.result

    def multiply(self, num):
        self.result *= num
        #        logging.info(f"Multiplied by {num}. Result: {self.result}")
        return self.result

    def divide(self, num):
        if num == 0:
            logging.error("Division by zero!")
            return None
        else:
            self.result /= num
            #            logging.info(f"Divided by {num}. Result: {self.result}")
            return self.result

    def clear(self):
        self.result = 0
        logging.info("Result cleared.")


if __name__ == "__main__":
    calc = Calculator()
    logging.info("Calculator initialized.")

    while True:
        try:
            # Ask user how many numbers they want to operate with
            num_count = input(
                "Enter how many numbers do you want to operate with (or enter 'q' to quit): "
            )

            # Check if the user wants to quit
            if num_count.lower() == "q":
                logging.info("Exiting the calculator.")
                break

            # Convert input to integer
            num_count = int(num_count)

            # Initialize an empty list to store numbers and operators
            expressions = []

            # Take user input for numbers and operators
            for i in range(num_count - 1):
                # only num_count - 1 operators are required for num_count numbers
                num = float(input(f"Enter number {i + 1}: "))
                operator = input(
                    f"Enter the operator (+, -, *, /) for numbers {i + 1}: "
                )
                expressions.append((num, operator))

            # Take input for the last number separately
            num = float(input(f"Enter number {num_count}: "))

            # Perform calculation based on numbers and operators
            for num, operator in expressions:
                if operator == "+":
                    calc.add(num)
                elif operator == "-":
                    calc.subtract(num)
                elif operator == "*":
                    calc.multiply(num)
                elif operator == "/":
                    calc.divide(num)
                else:
                    if num != 0:
                        calc.divide(num)
            else:
                logging.error("Division by zero is not allowed.")

            # Perform the operation with the last number
            last_operator = expressions[-1][
                1
            ]  # get the operator for the last calculation
            if last_operator == "+":
                calc.add(num)
            elif last_operator == "-":
                calc.subtract(num)
            elif last_operator == "*":
                calc.multiply(num)
            elif last_operator == "/":
                calc.divide(num)
            else:
                if num != 0:
                    calc.divide(num)
                else:
                    logging.error("Division by zero is not allowed.")
            # else:
            #     logging.error("Invalid operator.")

            calc.clear()

            choice = input("Do you want to make another calculation? (yes/no): ")
            if choice.lower() != "yes":
                logging.info("Exiting the calculator.")
                break

        except ValueError:
            logging.error("Invalid input! Please enter a valid number.")
