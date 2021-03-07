import string


def is_pangram(sentence):
    letters = list(string.ascii_lowercase)
    sentence = sentence.lower()
    for i in sentence:
        if i in letters:
            letters.remove(i)
    if not letters:
        return True
    else:
        return False
