import math

num_str = input("Enter a number: ")

try:
    num = float(num_str)
    rounded_up = math.ceil(num)
    print(f"The number rounded up is {rounded_up}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
