# VALIDATING USER INPUT
# Check that input is valid before attempting to convert.
'''user_choice = input("Enter a number: ")
if user_choice.isdigit():
    print("You enter the number:",user_choice)
else:
    print("You enter the wrong input. We think you enter the number in words please enter in numerical form.")'''
user_choice = input("Enter a number: ")
while user_choice.isdigit() == False:
    print("You didn't enter values in numeric form.")
    user_choice = input("Enter a number: ")
else:
    print("You entered:",user_choice)