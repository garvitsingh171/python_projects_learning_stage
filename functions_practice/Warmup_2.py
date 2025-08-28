# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    text = text.split()
    text1 = text[0][0]
    text2 = text[1][0]
    if text1 == text2:
        return True
    else:
        return False
print(animal_crackers("Lambda lamma"))