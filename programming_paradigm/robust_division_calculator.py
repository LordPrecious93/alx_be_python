# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to floats and perform division
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator / denominator
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

