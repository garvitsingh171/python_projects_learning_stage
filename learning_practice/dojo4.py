user_input = input().split()
user_input = user_input.reverse()
user_input_reverse = " ".join(user_input)
if user_input == user_input_reverse:
    print("Palindrome")
else:
    print("Not Palindrome")