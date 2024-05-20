import logging

logging.basicConfig(level=logging.INFO)


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        logging.info(f"Added {num}. Result: {self.result}")
        return self.result

    def subtract(self, num):
        self.result -= num
        logging.info(f"Subtracted {num}. Result: {self.result}")
        return self.result

    def multiply(self, num):
        self.result *= num
        logging.info(f"Multiplied by {num}. Result: {self.result}")
        return self.result

    def devide(self, num):
        if num == 0:
            logging.error("Division by zero!")
            return None
        else:
            self.result /= num
            logging.info(f"Divided by {num}. Result: {self.result}")
            return self.result
