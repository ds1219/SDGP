from nltk import tokenize
def textPreProcess(text):
    text=removeWikipedia(text)
    
    return tokenize.sent_tokenize(text)

def getKeywords(text):
    keywords = [['Facebook', 'IPO', 'January 1m 2012'],
                ['$5 Billion', '845 million', '2.7 Billion'],
                ['IPO', 'Zuckerberg', '22%', '57%'],
                ['$38', '$104 billion'],
                ['May 16', '25%', 'shares'],
                ['IPO', '$16 Billion', 'third-largest'],
                ['market capitalization', '19 Billion'],
                ['The New York Times', 'advertisers',],
                ['Jimmy Lee', 'JPMorgan Chase'],
                ['TechCrunch', 'new revenue streams'],
                ['May 18', 'Nasdaq', 'technical problems'],
                ['IPO Price', 'underwriters', '38.23', '$0.23', '$3.82'],
                ['financial press', 'dissapointment', 'opening'],
                ['IPO', 'record', 'trading volume'],
                ['May 25.2012', '$31.91', '16.5%'],
                ['May 22, 2012', 'regulators', 'Financial Industry Regulatory Authority', 'investigate', 'banks', 'Facebook', 'information', 'clients', 'general public'],
                ['William Galvin', 'Massachusetts Secretary of State', 'Morgan Stanley'],
                ['allegations', 'investors', 'lawsuits', 'class action suit', '$2.5 billion', 'losses', 'IPO'],
                ['Bloomberg', 'retail investors', '$630 Million', 'Facebook', 'stock'],
                ["Standard & Poor's", 'Facebook', 'S&P 500', 'December 21, 2013'],
                ['May 2, 2014', "Zuckerberg", 'motto'],
                ['moto', 'Zuckerberg', 'Buisiness Insider', 'interview']
                ]
    
    return(keywords)


def removeWikipedia(text):
    #https://stackoverflow.com/questions/67605758/how-to-match-and-remove-wikipedia-refences-with-python-and-re
    import re

    text = text.strip()
    text = re.sub("\[[0-9]+\]", '', text)
    return text