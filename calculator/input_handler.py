class InputHandler:
    """Handles and validates user inputs."""

    @staticmethod
    def get_number_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    @staticmethod
    def get_operator_input():
        valid_operations = ['+', '-', '*', '/', '**', 'sqrt']
        while True:
            operation = input("Enter an operation (+, -, *, /, **, sqrt): ").strip()
            if operation in valid_operations:
                return operation
            print("Invalid operation. Choose from +, -, *, /, **, sqrt.")

