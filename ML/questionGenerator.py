import torch
import spacy
from nltk import tokenize
import nltk
from transformers import T5ForConditionalGeneration, T5Tokenizer
from preproccessing import *

device = torch.device("cpu")

'''question_model = T5ForConditionalGeneration.from_pretrained(
    "./ramsrigouthamg-t5_squad_v1"
)'''

question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')

'''question_tokenizer = T5Tokenizer.from_pretrained("./ramsrigouthamg-t5_squad_v1")'''

question_tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_squad_v1')
question_model = question_model.to(device)

import nltk

nltk.download("punkt")
nltk.download("brown")
nltk.download("wordnet")
nltk.download("stopwords")

from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import string
import pke
import traceback





'''def getKeywords(text):
    keywords = []
    return keywords'''


def removeWikipedia(text):
    # https://stackoverflow.com/questions/67605758/how-to-match-and-remove-wikipedia-refences-with-python-and-re
    import re

    text = text.strip()
    text = re.sub("\[[0-9]+\]", "", text)
    return text




'''def postprocesstext (content):
    final=""
    for sent in sent_tokenize(content):
        sent = sent.capitalize()
        final = final +" "+sent
    return final'''

'''def textPreProcess(text):
    text = removeWikipedia(text)
    #text = tokenize.sent_tokenize(text)
    return tokenize.sent_tokenize(text)
    #return text'''


#keyword extraction
def getKeywords(text):
    '''keywords = []
    try:
        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(input=text, language="en")

        pos = {"PROPN", "NOUN"}

        stoplist = list(string.punctuation)
        stoplist += ["-lrb-", "-rrb-", "-lcb-", "-rcb-", "-lsb-", "-rsb-"]
        stoplist += stopwords.words("english")

        extractor.candidate_selection(pos=pos)

        extractor.candidate_weighting(alpha=1.1, threshold=0.75, method="average")
        keyphrases = extractor.get_n_best(n=10)

        for val in keyphrases:
            keywords.append(val[0])
    except:
        keywords = []
        traceback.print_exc()

    return keywords'''


    
    keywords = []
    try:
        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(input=text, language="en")

        pos = {"PROPN", "NOUN"}

        stoplist = list(string.punctuation)
        stoplist += ["-lrb-", "-rrb-", "-lcb-", "-rcb-", "-lsb-", "-rsb-"]
        stoplist += stopwords.words("english")

        extractor.candidate_selection(pos=pos)

        extractor.candidate_weighting(alpha=1.1, threshold=0.75, method="average")
        keyphrases = extractor.get_n_best(n=4)

        keywords = [['Meta Platforms'], ['Facebook'], ['Mark Zuckerberg'], ['Cambridge Analytica data scandal']]

        for val in keyphrases:
            # tokenize the keyphrase and add it to the keywords list
            keywords.append(nltk.word_tokenize(val[0]))
    except:
        keywords = []
        traceback.print_exc()

    return keywords
    
#keywords = getKeywords(text)
#print("keywords: ", keywords)

def get_question(context, answer, model, tokenizer):
    text = "context: {} answer: {}".format(context, answer)
    encoding = tokenizer.encode_plus(
        text,
        max_length=384,
        pad_to_max_length=False,
        truncation=True,
        return_tensors="pt",
    ).to(device)
    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    outs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        early_stopping=True,
        num_beams=5,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        max_length=512,
    )

    dec = [tokenizer.decode(ids, skip_special_tokens=True) for ids in outs]

    Question = dec[0].replace("question:", "")
    Question = Question.strip()
    return Question


def generate(text):
    #text = textPreProcess(text)
    keywords = getKeywords(text)
    print("keywords: ", keywords)
    QA = []
    
    for key in range(0, len(keywords)):
        # print(keywords[key])
        # print(text[key])
        for k in range(0, len(keywords[key])):
            answer = keywords[key][k]
            sentence = text[key]
            ques = get_question(sentence, answer, question_model, question_tokenizer)
            QA.append(ques)

    #print(QA)
    answers = []
    for x in keywords:
        answers += x
    #answer = keywords
    return QA, answers




if __name__ == "__main__":

    text = """ Facebook is an online social media and social networking service owned by American technology giant Meta Platforms. Created in 2004 by Mark Zuckerberg with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes, its name derives from the face book directories often given to American university students. Membership was initially limited to only Harvard students, gradually expanding to other North American universities and, since 2006, anyone over 13 years old. As of December 2022, Facebook claimed 2.96 billion monthly active users, and ranked third worldwide among the most visited websites. It was the most downloaded mobile app of the 2010s.[8]

Facebook can be accessed from devices with Internet connectivity, such as personal computers, tablets and smartphones. After registering, users can create a profile revealing information about themselves. They can post text, photos and multimedia which are shared with any other users who have agreed to be their "friend" or, with different privacy settings, publicly. Users can also communicate directly with each other with Messenger, join common-interest groups, and receive notifications on the activities of their Facebook friends and the pages they follow.

The subject of numerous controversies, Facebook has often been criticized over issues such as user privacy (as with the Cambridge Analytica data scandal), political manipulation (as with the 2016 U.S. elections) and mass surveillance. Posts originating from the Facebook page of Breitbart News, a media organization previously affiliated with Cambridge Analytica, are currently among the most widely shared political content on Facebook. Facebook has also been subject to criticism over psychological effects such as addiction and low self-esteem, and various controversies over content such as fake news, conspiracy theories, copyright infringement, and hate speech. Commentators have accused Facebook of willingly facilitating the spread of such content, as well as exaggerating its number of users to appeal to advertisers."""
    
    
    '''text = postprocesstext(text)
    text= text.strip()'''
    questions, answers = generate(text)

    for i in range(0, len(answers)):
        print(f"Q{i+1}: {questions[i]} - {answers[i]}")

    #print(answer)

    

