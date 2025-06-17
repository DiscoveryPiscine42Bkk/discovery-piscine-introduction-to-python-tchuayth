Number = int(input("Enter a number: "))
print(f"Multiplication table for {Number}:")
for i in range(1, 21):
    print(f"{Number} x {i} = {Number * i}")
