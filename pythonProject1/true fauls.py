def check_values(val1, val2):
    # Check if the values are equal
    if val1 == val2:
        return True

    # Check if the sum or difference is 5
    if abs(val1 - val2) == 5 or val1 + val2 == 5:
        return True

    # If none of the conditions are met, return False
    return False

# Example usage:
value1 = int(input("Enter the first integer: "))
value2 = int(input("Enter the second integer: "))

result = check_values(value1, value2)

print(f"Result: {result}")
