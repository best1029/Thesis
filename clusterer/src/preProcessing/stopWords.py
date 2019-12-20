from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from src.inOut import list2file, file2list
from src.logger import logger

import src.config as conf

def getStopWords(docs = None, idf_limit_min = conf.default_idf_limit_min):

    print("get stopwords mit")

    stop_words = stopwords.words('german')
    logger.info("Basic-Stopwords loaded")

    if docs is not None:
        calculateCustomStopWords(docs, idf_limit_min)
  
    specific_stopwords = file2list(conf.path_stopwords_ger)
    logger.info("Custom-Stopwords loaded")
    
    stop_words.extend(specific_stopwords)

    return stop_words

def calculateCustomStopWords(docs, limit_min = conf.default_idf_limit_min):

    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(docs.values())

    idf = vectorizer.idf_

    word_idf = dict(zip(vectorizer.get_feature_names(), idf))

    res = []
    for word in word_idf:
        if word_idf[word] < limit_min:
            res.append(word)
    logger.info("calculated Custom-Stopwords")
    list2file(res, conf.path_stopwords_ger)
    logger.info("saved Custom-Stopwords to File")