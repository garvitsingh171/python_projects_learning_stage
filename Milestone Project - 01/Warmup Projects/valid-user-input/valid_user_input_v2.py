# Now, we are trying to clear the ouput once out input is not valid acc to program.
import os
def clear_output():
    os.system('cls')
x = int(input("Enter a Number:"))
while x != 2:
    x = int(input("Enter a Number:"))
else:
    clear_output()
    print("You are dumb!!")