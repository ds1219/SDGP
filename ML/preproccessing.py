from nltk import tokenize


def textPreProcess(text):
    text = removeWikipedia(text)

    return tokenize.sent_tokenize(text)


def removeWikipedia(text):
    # https://stackoverflow.com/questions/67605758/how-to-match-and-remove-wikipedia-refences-with-python-and-re
    import re

    text = text.strip()
    text = re.sub("\[[0-9]+\]", "", text)
    return text
