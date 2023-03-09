import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
from tqdm import tqdm

device = torch.device("cpu")

torch.manual_seed(42)

question_model = T5ForConditionalGeneration.from_pretrained('./ramsrigouthamg-t5_squad_v1')
question_tokenizer = T5Tokenizer.from_pretrained('./ramsrigouthamg-t5_squad_v1')
question_model = question_model.to(device)

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

def generate(text, keywords: list,):
  textlen = len(text)
  QA = []
  for i in tqdm(range(0,len(keywords))):
    answer = keywords[i]
    ques = get_question(text,answer,question_model,question_tokenizer)
    QA.append(ques)
  return QA

# run at will
text = """In the year 1878 I took my degree of
Doctor of Medicine of the University of
London, and proceeded to Netley to go
through the course prescribed for surgeons in the army. Having completed my studies
there, I was duly attached to the Fifth Northumberland Fusiliers as Assistant Surgeon. The regiment
was stationed in India at the time, and before I
could join it, the second Afghan war had broken
out. On landing at Bombay, I learned that my corps
had advanced through the passes, and was already
deep in the enemy’s country. I followed, however,
with many other officers who were in the same
situation as myself, and succeeded in reaching Candahar in safety, where I found my regiment, and at
once entered upon my new duties."""

keywords = ['surgeons', 'Bombay', 'India', 'the regiment']

Questions = generate(text, keywords)

for i in range(0, len(keywords)):
  print(f"{keywords[i]} - {Questions[i]}")
