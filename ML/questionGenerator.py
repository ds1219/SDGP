import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
from preproccessing import *
device = torch.device("cpu")

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

def generate(text):
  text = textPreProcess(text)
  keywords = getKeywords(text)
  QA = []

  for key in range(0,len(keywords)):
    for k in range(0,len(keywords[key])):
      answer = keywords[key][k]
      scentence = text[key]
      ques = get_question(scentence,answer,question_model,question_tokenizer)
      print(f"Done: {key},{k}")
      QA.append(ques)
  
  answers = []
  for x in keywords:
     answers += x
  return QA,answers

# run at will
text = """Facebook filed for an initial public offering (IPO) on January 1, 2012.[26] The preliminary prospectus stated that the company sought to raise $5 billion, had 845 million monthly active users, and a website accruing 2.7 billion likes and comments daily.[27] After the IPO, Zuckerberg would retain a 22% ownership share in Facebook and would own 57% of the voting shares.[28]

Underwriters valued the shares at $38 each, valuing the company at $104 billion, the largest valuation to date for a newly public company.[29] On May 16, one day before the IPO, Facebook announced it would sell 25% more shares than originally planned due to high demand.[30] The IPO raised $16 billion, making it the third-largest in US history (slightly ahead of AT&T Wireless and behind only General Motors and Visa). The stock price left the company with a higher market capitalization than all but a few U.S. corporations—surpassing heavyweights such as Amazon, McDonald's, Disney, and Kraft Foods—and made Zuckerberg's stock worth $19 billion.[31][32] The New York Times stated that the offering overcame questions about Facebook's difficulties in attracting advertisers to transform the company into a "must-own stock". Jimmy Lee of JPMorgan Chase described it as "the next great blue-chip".[31] Writers at TechCrunch, on the other hand, expressed skepticism, stating, "That's a big multiple to live up to, and Facebook will likely need to add bold new revenue streams to justify the mammoth valuation."[33]

Trading in the stock, which began on May 18, was delayed that day due to technical problems with the Nasdaq exchange.[34] The stock struggled to stay above the IPO price for most of the day, forcing underwriters to buy back shares to support the price.[35] At closing bell, shares were valued at $38.23,[36] only $0.23 above the IPO price and down $3.82 from the opening bell value. The opening was widely described by the financial press as a disappointment.[37] The stock nonetheless set a new record for trading volume of an IPO.[38] On May 25, 2012, the stock ended its first full week of trading at $31.91, a 16.5% decline.[39]

On May 22, 2012, regulators from Wall Street's Financial Industry Regulatory Authority announced that they had begun to investigate whether banks underwriting Facebook had improperly shared information only with select clients rather than the general public. Massachusetts Secretary of State William Galvin subpoenaed Morgan Stanley over the same issue.[40] The allegations sparked "fury" among some investors and led to the immediate filing of several lawsuits, one of them a class action suit claiming more than $2.5 billion in losses due to the IPO.[41] Bloomberg estimated that retail investors may have lost approximately $630 million on Facebook stock since its debut.[42] Standard & Poor's added Facebook to its S&P 500 index on December 21, 2013.[43]

On May 2, 2014, Zuckerberg announced that the company would be changing its internal motto from "Move fast and break things" to "Move fast with stable infrastructure".[44][45] The earlier motto had been described as Zuckerberg's "prime directive to his developers and team" in a 2009 interview in Business Insider, in which he also said, "Unless you are breaking stuff, you are not moving fast enough."[46]"""
questions, answers = generate(text)

for i in range(0, len(answers)):
   print(f"Q{i+1}: {questions[i]} - {answers[i]}")