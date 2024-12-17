from .operations import Operations
from .input_handler import InputHandler

class Calculator:
    """Advanced Calculator Class."""
    
    def __init__(self):
        self.operations = Operations()
        self.input_handler = InputHandler()

    def run(self):
        print("Welcome to the Advanced Calculator!\n")
        while True:
            operator = self.input_handler.get_operator_input()

            if operator == 'sqrt':
                num1 = self.input_handler.get_number_input("Enter the number: ")
                result = self.operations.square_root(num1)
            else:
                num1 = self.input_handler.get_number_input("Enter the first number: ")
                num2 = self.input_handler.get_number_input("Enter the second number: ")

                if operator == '+':
                    result = self.operations.add(num1, num2)
                elif operator == '-':
                    result = self.operations.subtract(num1, num2)
                elif operator == '*':
                    result = self.operations.multiply(num1, num2)
                elif operator == '/':
                    try:
                        result = self.operations.divide(num1, num2)
                    except ValueError as e:
                        print(e)
                        continue
                elif operator == '**':
                    result = self.operations.power(num1, num2)

            print(f"Result: {result}")
            
            cont = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break

