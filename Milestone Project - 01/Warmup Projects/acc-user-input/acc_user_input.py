# Accepting User Input
# Creating function that takes in an input from user and returns the result in the correct data type. Be careful when using the input() function, running that cell twice without providing an input value will cause python to get hung up waiting for the initial value on the first run. You will notice an In[*] next to the cell if it gets stuck, in which case, simply restart the kernel and re-run any necessary cells.
def check_input(User_data):
    if type(User_data) == type("Hello"):
        return str(User_data)
    else:
        return "It is not a number. Please enter number"
result = input("Enter a number: ")
print(check_input(result))