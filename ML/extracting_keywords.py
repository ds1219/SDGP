import nltk

nltk.download("punkt")
nltk.download("brown")
nltk.download("wordnet")
nltk.download("stopwords")
from nltk.corpus import stopwords
import string
import pke
import traceback


# lecture note input
text = """• Based on the distributed model having an architecture that
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


# keyword extraction
def get_keywords(content):
    out = []
    try:
        extractor = pke.unsupervised.MultipartiteRank()
        extractor.load_document(input=content, language="en")

        pos = {"PROPN", "NOUN"}

        stoplist = list(string.punctuation)
        stoplist += ["-lrb-", "-rrb-", "-lcb-", "-rcb-", "-lsb-", "-rsb-"]
        stoplist += stopwords.words("english")

        extractor.candidate_selection(pos=pos)

        extractor.candidate_weighting(alpha=1.1, threshold=0.75, method="average")
        keyphrases = extractor.get_n_best(n=15)

        for val in keyphrases:
            out.append(val[0])
    except:
        out = []
        traceback.print_exc()

    return out


keywords = get_keywords(text)
print("keywords: ", keywords)
