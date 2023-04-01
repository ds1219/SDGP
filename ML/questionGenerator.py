import torch
import spacy
from nltk import tokenize
import nltk
from transformers import T5ForConditionalGeneration, T5Tokenizer
from preproccessing import *
from extracting_keywords import get_keywords

device = torch.device("cpu")

question_model = T5ForConditionalGeneration.from_pretrained(
    "ramsrigouthamg/t5_squad_v1"
)

question_tokenizer = T5Tokenizer.from_pretrained("ramsrigouthamg/t5_squad_v1")
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


def removeWikipedia(text):
    # https://stackoverflow.com/questions/67605758/how-to-match-and-remove-wikipedia-refences-with-python-and-re
    import re

    text = text.strip()
    text = re.sub("\[[0-9]+\]", "", text)
    return text


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
    text = textPreProcess(text)
    keywords = []
    for scentence in text:
        keywords.append(get_keywords(scentence))

    QA = []

    for key in range(0, len(keywords)):
        for k in range(0, len(keywords[key])):
            answer = keywords[key][k]
            sentence = text[key]
            ques = get_question(sentence, answer, question_model, question_tokenizer)
            QA.append(ques)

    answers = []
    for x in keywords:
        answers += x
    return QA, answers
