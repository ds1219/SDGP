import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
from preproccessing import *
device = torch.device("cpu")

question_model = T5ForConditionalGeneration.from_pretrained('./ramsrigouthamg-t5_squad_v1')
question_tokenizer = T5Tokenizer.from_pretrained('./ramsrigouthamg-t5_squad_v1')
question_model = question_model.to(device)

import nltk
nltk.download('punkt')
nltk.download('brown')
nltk.download('wordnet')

from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize

def get_question(context,answer,model,tokenizer):
    text = "context: {} answer: {}".format(context,answer)
    encoding = tokenizer.encode_plus(text,max_length=384, pad_to_max_length=False,truncation=True, return_tensors="pt").to(device)
    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    outs = model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=5,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  max_length=512)

    dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]

    Question = dec[0].replace("question:","")
    Question= Question.strip()
    return Question

def generate(text):
  text = textPreProcess(text)
  keywords = getKeywords(text)
  QA = []

  for key in range(0,len(keywords)):
    #print(keywords[key])
    #print(text[key])
    for k in range(0,len(keywords[key])):
      answer = keywords[key][k]
      scentence = text[key]
      ques = get_question(scentence,answer,question_model,question_tokenizer)
      QA.append(ques)
  
  answers = []
  for x in keywords:
     answers += x
  return QA,answers

if __name__ == '__main__':

  text = ''' '''
  questions, answers = generate(text)

  for i in range(0, len(answers)):
    print(f"Q{i+1}: {questions[i]} - {answers[i]}")
