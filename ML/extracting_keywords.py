
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
from textwrap3 import wrap
import random
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('brown')
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import pke
import traceback
from flashtext import KeywordProcessor

#.....copy and pasting text.....
note = """• Based on the distributed model having an architecture that
partitions tasks or workloads between the providers of a
resource or service (server) and service requesters (client) that
communicate over computer network
• Server host runs one or more server programs which share their
resources with clients
• Client does not share any of its resources, but requests a server's
content or service function
• Server software accepts requests for a service from client
software and returns the results to the client
• Client-server architecture separates a program from the device it
is accessed from"""


# for wrp in wrap(note, 150):
#   print (wrp)
# print ("\n")

#....summarizarion with T5....

sum_model = T5ForConditionalGeneration.from_pretrained('t5-base')
sum_tokenizer = T5Tokenizer.from_pretrained('t5-base')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
sum_model = sum_model.to(device)



def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

set_seed(42)


def postprocesstext (content):
  final=""
  for sent in sent_tokenize(content):
    sent = sent.capitalize()
    final = final +" "+sent
  return final


def summarizer(note,model,tokenizer):
  note = note.strip().replace("\n"," ")
  note = "summarize: "+note
  # print (note)
  max_len = 512
  encoding = tokenizer.encode_plus(note,max_length=max_len, pad_to_max_length=False,truncation=True, return_tensors="pt").to(device)

  input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

  outs = model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=3,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  min_length = 75,
                                  max_length=300)


  dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
  summary = dec[0]
  summary = postprocesstext(summary)
  summary= summary.strip()

  return summary


summarized_note = summarizer(note,sum_model,sum_tokenizer)


# print ("\noriginal Text >>")
# for wrp in wrap(note, 150):
#   print (wrp)
# print ("\n")
# print ("Summarized Text >>")
# for wrp in wrap(summarized_note, 150):
#   print (wrp)
# print ("\n")

#...key word extraction....
def get_nouns_multipartite(content):
    out=[]
    try:
        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(input=content,language='en')
        
        pos = {'PROPN','NOUN'}
        
        stoplist = list(string.punctuation)
        stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
        stoplist += stopwords.words('english')
       
        extractor.candidate_selection(pos=pos)
      
        extractor.candidate_weighting(alpha=1.1,
                                      threshold=0.75,
                                      method='average')
        keyphrases = extractor.get_n_best(n=15)
        

        for val in keyphrases:
            out.append(val[0])
    except:
        out = []
        traceback.print_exc()

    return out



def get_keywords(originalnote,summarynote):
  keywords = get_nouns_multipartite(originalnote)
  print ("unsummarized keywords: ",keywords)
  keyword_processor = KeywordProcessor()
  for keyword in keywords:
    keyword_processor.add_keyword(keyword)

  found_keywords = keyword_processor.extract_keywords(summarynote)
  found_keywords = list(set(found_keywords))
  print ("summarized keywords: ",found_keywords)

  important_keywords =[]
  for keyword in keywords:
    if keyword in found_keywords:
      important_keywords.append(keyword)

  return important_keywords[:4]


imp_keywords = get_keywords(note,summarized_note)
print (imp_keywords)
