while True:
    prompt = "What you gotta say? : " if 'user_input' not in locals() else "I got that! Anything else? : "
    user_input = input(prompt)
    if user_input == "STOP":
        break
