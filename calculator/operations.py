class Operations:
    """Class for mathematical operations."""
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def square_root(a):
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return a ** 0.5

