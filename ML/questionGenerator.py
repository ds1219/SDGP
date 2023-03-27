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
        keyphrases = extractor.get_n_best(n=200)

        for val in keyphrases:
            keywords.append(val[0])
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

    text = """Almost all children have times when their behavior veers out of control. They may speed about in constant motion, make noise nonstop, refuse to wait their turn, and crash into everything around them. At other times they may drift as if in a daydream, failing to pay attention or finish what they start.

However, for some children, these kinds of behaviors are more than an occasional problem. Children with attention-deficit/hyperactivity disorder (ADHD) have behavior problems that are so frequent and/or severe that they interfere with their ability to live normal lives. These children often have trouble getting along with siblings and other children at school, at home, and in other settings. Those who have trouble paying attention usually have trouble learning. Some have an impulsive nature and this may put them in actual physical danger. Because children with ADHD have difficulty controlling their behavior, they may be labeled as “bad kids” or “space cadets.” Left untreated, more severe forms of ADHD can lead to serious, lifelong problems such as poor grades in school, run-ins with the law, failed relationships, substance abuse and the inability to keep a job.

What is ADHD?
ADHD is a condition of the brain that makes it difficult for children to control their behavior. It is one of the most common chronic conditions of childhood. It affects 4% to 12% of school-aged children. About 3 times more boys than girls are diagnosed with ADHD.

Child lost in daydreamWhat are the symptoms of ADHD?
ADHD includes 3 behavior symptoms: inattention, hyperactivity, and impulsivity. A child with inattention symptoms may have the following behaviors:

Has a hard time paying attention, daydreams
Does not seem to listen
Is easily distracted from work or play
Does not seem to care about details, makes careless mistakes
Does not follow through on instructions or finish tasks
Is disorganized
Loses a lot of important things
Forgets things
Does not want to do things that require ongoing mental effort
A child with hyperactivity symptoms may have the following behaviors:

Is in constant motion, as if “driven by a motor”
Cannot stay seated
Squirms and fidgets
Talks too much
Runs, jumps, and climbs when this is not permitted
Cannot play quietly (video games do not count)
A child with impulsivity symptoms may have the following behaviors:

Acts and speaks without thinking
May run into the street without looking for traffic first
Has trouble taking turns
Cannot wait for things
Calls out answers before the question is complete
Interrupts others
What is the difference between ADD vs. ADHD?
ADD stands for Attention Deficit Disorder. This is an old term that is now officially called Attention Deficit Hyperactivity Disorder, Inattentive Type. More on this will discussed below.
 """
    
    
    '''text = postprocesstext(text)
    text= text.strip()'''
    questions, answers = generate(text)

    '''for i in range(0, len(answers)):
        print(f"Q{i+1}: {questions[i]} - {answers[i]}")'''

    #print(answer)

