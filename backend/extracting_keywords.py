"""
Code has been Adapted From:
Alto, A. (2015). Answer to ‘Extracting all Nouns from a text file using nltk’. Stack Overflow. Available from https://stackoverflow.com/a/33588238 [Accessed 5 April 2023].
"""
from textblob import TextBlob

def get_keywords(content):
    blob = TextBlob(content)
    return [phrase for phrase in blob.noun_phrases if len(phrase.split())]