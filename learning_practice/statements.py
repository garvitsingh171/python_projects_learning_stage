user_input = input()
user_input_list = list(user_input)
print(user_input)
list_reverse = user_input_list[::-1]
print(list_reverse)
reversed_word = ''.join(list_reverse)
print(reversed_word)
if user_input == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")