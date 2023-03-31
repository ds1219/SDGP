import nltk

nltk.download("punkt")
nltk.download("brown")
nltk.download("wordnet")
nltk.download("stopwords")
from nltk.corpus import stopwords
import string
import pke
import traceback

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
