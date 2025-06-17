while True:
    user_input = input("Enter something (type 'STOP' to quit): ")
    if user_input == "STOP":
        print("Program stopped.")
        break
    else:
        print("You said:", user_input)
