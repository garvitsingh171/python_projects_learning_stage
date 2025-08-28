with open('myfile.txt', mode='a') as f:
    f.write('\nThis the fourth line')
with open('myfile.txt', mode='r') as f:
    print(f.read())