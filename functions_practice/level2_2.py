# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(word):
    modified_word = ""
    for letter in word:
        modified_word += letter*3
    return modified_word
print(paper_doll("Hello"))