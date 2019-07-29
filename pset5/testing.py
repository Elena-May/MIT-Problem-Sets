"""
import string

phrase = 'love COWS'
text = 'I... LOVE cows!!//'

def is_phrase_in(text, phrase):
    translator = str.maketrans('', '', string.punctuation)
    phrase = phrase.translate(translator).lower().split()
    text = text.translate(translator).lower().split()
    textphrase = []

    for item in range(len(text)):
        for word in range(len(phrase)):
            if text[item] == phrase[word]:
                    textphrase.append(text[item])

    textphrase = " ".join(textphrase)
    phrase = " ".join(phrase)

    if textphrase == phrase:
        return True
    else:
        return False





final = is_phrase_in(text,phrase)

print(final)

"""

from datetime import datetime

time_now = datetime.now()

print(time_now)