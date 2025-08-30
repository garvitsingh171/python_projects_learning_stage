# Function to Display Information
# Creating a function that displays a list for the user
    # x = x + 1

user_input = list(map(str,input("Enter your items with spaces: ").split()))

for i in range(0,len(user_input)):
    print( f"{i+1} : {user_input[i]}")
# print(user_input)