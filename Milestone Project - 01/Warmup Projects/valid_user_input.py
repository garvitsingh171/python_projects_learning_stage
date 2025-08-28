# VALIDATING USER INPUT
# Check that input is valid before attempting to convert.
user_choice = input("Enter a number: ")
if user_choice.isdigit():
    print("You enter the number:",user_choice)
else:
    print("You enter the wrong input. We think you enter the number in words please enter in numerical form.")