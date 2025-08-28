hello = "Hello, World!"
print(hello)
# This is a comment
print(hello[0])  # H
print(hello[7])  # W
print(hello[-1])  # !
print(hello[0:5])  # Hello
print(hello[7:12])  # World
print(hello[7:])  # World!
print(hello[:5])  # Hello
print(hello[0:5:2])  # Hlo #0 to 5 with step 2
print(hello[::])  # Hello, World! (full string)
print(hello[::2])  # Hlo ol!
print(hello[::-1])  # !dlroW ,olleH (reversed string)
# Slicing with negative indices
print(hello[-6:-1])  # World
print(hello[-6:])  # World!
# Slicing with step
print(hello[::3])  # Hl r! (every third character)
# Slicing with step and negative indices
print(hello[::-2])  # !lo olH (every second character in reverse)
# Concatenate strings
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Hello, Alice!
print(greeting * 3)  # HelloHelloHello
# String length
print(len(hello))  # 13
print(len(greeting))  # 5
print(len(name))  # 5
print(len(full_greeting))  # 20
print(full_greeting.upper())  # HELLO, ALICE!
print(full_greeting.lower())  # hello, alice!
# String methods
print(full_greeting.replace("Alice", "Bob"))  # Hello, Bob!
print(full_greeting.find("Alice"))  # 7 (index of "Alice")
print(full_greeting.index("Alice"))  # 7 (index of "Alice")
print(full_greeting.count("l"))  # 3 (count of 'l' in the string)
# Check if a substring exists
print("Alice" in full_greeting)  # True
print(full_greeting)
# Check if a string starts or ends with a substring
print(full_greeting.startswith("Hello"))  # True
print(full_greeting.endswith("!"))  # True
# Split and join strings
words = full_greeting.split(", ")
print(words)  # ['Hello', 'Alice!']
joined = " - ".join(words)
print(joined)  # Hello - Alice!
# Insert another string with .format()
formatted_greeting = "Greetings, {}!".format(name)
print(formatted_greeting)  # Greetings, Alice!
formatted_greeting2 = "Hello, Alice! {} is a great name.".format(name)
print(formatted_greeting2)  # Hello, Alice! Alice is a great name.
# f-strings (formatted string literals)
f_greeting = f"Hello, {name}!"
print(f_greeting)  # Hello, Alice!
# f-strings with expressions
f_greeting2 = f"Hello, {name}! The length of your name is {len(name)}."
print(f_greeting2)  # Hello, Alice! The length of your name is 5.
# f-strings with calculations
f_greeting3 = f"Hello, {name}! In 5 years, you will be {30 + 5} years old."
print(f_greeting3)  # Hello, Alice! In 5 years, you will be 35 years old.
# f-strings with method calls
f_greeting4 = f"Hello, {name}! Your name in uppercase is {name.upper()}."
print(f_greeting4)  # Hello, Alice! Your name in uppercase is ALICE.
# f-strings with multiple variables
age = 30
f_greeting5 = f"Hello, {name}! You are {age} years old."
print(f_greeting5)  # Hello, Alice! You are 30 years old.
# f-strings with lists
fruits = ["apple", "banana", "cherry"]
f_fruits = f"My favorite fruits are: {', '.join(fruits)}."
print(f_fruits)  # My favorite fruits are: apple, banana, cherry.
# f-strings with dictionaries
person = {"name": "Alice", "age": 30}
f_person = f"Hello, {person['name']}! You are {person['age']} years old."
print(f_person)  # Hello, Alice! You are 30 years old.
# formatting with placeholders
print("Hello, %s!" % name)  # Hello, Alice!
print("Hello, {}!".format(name))  # Hello, Alice!
print(f"Hello, {name}!")  # Hello, Alice!
# Using the format method with positional and keyword arguments
formatted_string = "Hello, {0}! You are {1} years old.".format(name, age)
print(formatted_string)  # Hello, Alice! You are 30 years old.
b = "Python Bootcamp"
print(b[-7:])
score = 95
print("Your score is: " + str(score))  # This will raise an error because score is an integer
# Correcting the above line by converting score to a string