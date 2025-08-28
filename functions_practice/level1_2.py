# MASTER YODA: Given a sentence, return a sentence with the words reversed
# To be reviewed
def master_yoda(sentence):
    sentence = sentence.split()
    sentence = sentence[::-1]
    sentence = ' '.join(sentence)
    return sentence
print(master_yoda("Hello my name is"))