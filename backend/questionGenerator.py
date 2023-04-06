"""
Code has been Adapted From:
Goutham, R. (2021). Question Generation Using Natural Language Processing. YouTube. Available from https://www.youtube.com/watch?v=hoCi_bJHyb8&t=18s [Accessed 5 April 2023].
"""
import torch
import spacy
from nltk import tokenize
import nltk
from transformers import T5ForConditionalGeneration, T5Tokenizer
from preproccessing import *
from extracting_keywords import get_keywords
from collections import OrderedDict
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
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
import numpy as np
from sense2vec import Sense2Vec
from similarity.normalized_levenshtein import NormalizedLevenshtein

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

question_model = T5ForConditionalGeneration.from_pretrained(
    "ramsrigouthamg/t5_squad_v1"
)

question_tokenizer = T5Tokenizer.from_pretrained("ramsrigouthamg/t5_squad_v1")
question_model = question_model.to(device)


def removeWikipedia(text):
    # https://stackoverflow.com/questions/67605758/how-to-match-and-remove-wikipedia-refences-with-python-and-re
    import re

    text = text.strip()
    text = re.sub("\[[0-9]+\]", "", text)
    return text


def get_question(context, answer, model, tokenizer):

    # validates the inputs
    if not isinstance(context, str):
        raise ValueError("context must be a string")
    if not isinstance(answer, str):
        raise ValueError("answer must be a string")

    input_text = "context: {} answer: {}".format(context, answer)  # format input

    encoding = tokenizer.encode_plus(
        input_text,
        max_length=384,
        pad_to_max_length=False,
        truncation=True,
        return_tensors="pt",
    ).to(device)
    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    try:
        generated_sequences = model.generate(  # generates the questions
            input_ids=input_ids,
            attention_mask=attention_mask,
            early_stopping=True,
            num_beams=5,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            max_length=512,
        )

        decoded_sequences = [
            tokenizer.decode(ids, skip_special_tokens=True)
            for ids in generated_sequences
        ]

        generated_question = decoded_sequences[0].replace("question:", "").strip()
        return generated_question

    except Exception as e:
        raise ValueError(f"An error occurred while generating the question: {str(e)}")


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


# generating wrong answers
s2v = Sense2Vec().from_disk("s2v_old")


sentence_transformer_model = SentenceTransformer("msmarco-distilbert-base-v3")

normalized_levenshtein = NormalizedLevenshtein()


def filter_same_sense_words(original, wordlist):
    filtered_words = []
    base_sense = original.split("|")[1]
    for eachword in wordlist:
        if eachword[0].split("|")[1] == base_sense:
            filtered_words.append(
                eachword[0].split("|")[0].replace("_", " ").title().strip()
            )
    return filtered_words


def get_highest_similarity_score(wordlist, wrd):
    score = []
    for each in wordlist:
        score.append(normalized_levenshtein.similarity(each.lower(), wrd.lower()))
    return max(score)


def sense2vec_get_words(word, s2v, topn, question):
    output = []
    try:
        sense = s2v.get_best_sense(
            word,
            senses=[
                "NOUN",
                "PERSON",
                "PRODUCT",
                "LOC",
                "ORG",
                "EVENT",
                "NORP",
                "WORK OF ART",
                "FAC",
                "GPE",
                "NUM",
                "FACILITY",
            ],
        )
        most_similar = s2v.most_similar(sense, n=topn)
        output = filter_same_sense_words(sense, most_similar)

    except:
        output = []

    threshold = 0.6
    final = [word]
    checklist = question.split()
    for x in output:
        if (
            get_highest_similarity_score(final, x) < threshold
            and x not in final
            and x not in checklist
        ):
            final.append(x)

    return final[1:]


def mmr(doc_embedding, word_embeddings, words, top_n, lambda_param):

    # extract similarity within words and between words and the text
    word_doc_similarity = cosine_similarity(word_embeddings, doc_embedding)
    word_similarity = cosine_similarity(word_embeddings)

    # Initialize candidates and already choose best keyword/keyphrase
    keywords_idx = [np.argmax(word_doc_similarity)]
    candidates_idx = [i for i in range(len(words)) if i != keywords_idx[0]]

    for _ in range(top_n - 1):
        # Extract similarities within candidates and
        # between candidates and selected keywords/phrases
        candidate_similarities = word_doc_similarity[candidates_idx, :]
        target_similarities = np.max(
            word_similarity[candidates_idx][:, keywords_idx], axis=1
        )

        # calculates MMR
        mmr = (lambda_param) * candidate_similarities - (
            1 - lambda_param
        ) * target_similarities.reshape(-1, 1)
        mmr_idx = candidates_idx[np.argmax(mmr)]

        keywords_idx.append(mmr_idx)
        candidates_idx.remove(mmr_idx)

    return [words[idx] for idx in keywords_idx]


def get_distractors_wordnet(word):
    distractors = []
    try:
        syn = wn.synsets(word, "n")[0]
        word = word.lower()
        orig_word = word
        if len(word.split()) > 0:
            word = word.replace(" ", "_")
        hypernym = syn.hypernyms()
        if len(hypernym) == 0:
            return distractors
        for item in hypernym[0].hyponyms():
            name = item.lemmas()[0].name()
            if name == orig_word:
                continue
            name = name.replace("_", " ")
            name = " ".join(w.capitalize() for w in name.split())
            if name is not None and name not in distractors:
                distractors.append(name)
    except:
        print("distractors not found")
    return distractors


def get_distractors(
    word, origsentence, sense2vecmodel, sentencemodel, top_n, lambdaval
):
    distractors = sense2vec_get_words(word, sense2vecmodel, top_n, origsentence)

    if len(distractors) == 0:
        return distractors
    distractors_new = [word.capitalize()]
    distractors_new.extend(distractors)

    embedding_sentence = origsentence + " " + word.capitalize()
    keyword_embedding = sentencemodel.encode([embedding_sentence])
    distractor_embeddings = sentencemodel.encode(distractors_new)

    max_keywords = min(len(distractors_new), 3)
    filtered_keywords = mmr(
        keyword_embedding,
        distractor_embeddings,
        distractors_new,
        max_keywords,
        lambdaval,
    )
    final = [word.capitalize()]
    for wrd in filtered_keywords:
        if wrd.lower() != word.lower():
            final.append(wrd.capitalize())
    final = final[1:]
    return final


def getQAs(text):
    questions, answers = generate(text)
    ouput = []

    for i in range(0, len(answers)):
        sent = questions[i]
        keyword = answers[i]
        distractors = get_distractors(
            keyword, sent, s2v, sentence_transformer_model, 40, 0.2
        )
        if len(distractors) > 0:
            distractors = " | ".join(distractors)
            ouput.append([questions[i], answers[i], distractors])

    return ouput


if __name__ == "__main__":
    text = """In the year 1878 I took my degree of
Doctor of Medicine of the University of
London, and proceeded to Netley to go
through the course prescribed for surgeons in the army"""
    print(getQAs(text))
