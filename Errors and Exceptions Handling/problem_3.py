def ask():

    while True:
        try:
            user_input = int(input('Enter the integer: '))
        except:
            print('You did not enter the integer')
            continue
        else:
            print(user_input**2)

print(ask())

