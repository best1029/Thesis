import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

import src.config as conf

def getTfIdf(df_documente, min_ngram, max_ngram):
    content = df_documente["content"]

    vectorizer = TfidfVectorizer(ngram_range=(min_ngram, max_ngram))
    matrix = vectorizer.fit_transform(content)

    idf = vectorizer.idf_
    word_idf = dict(zip(vectorizer.get_feature_names(), idf))
    words = [w for w in word_idf if word_idf[w] >= conf.default_idf_limit_min and word_idf[w] <= conf.default_idf_limi_max]

    domains = df_documente["domain"]
    vecs = matrix.toarray()
    
    words = vectorizer.get_feature_names()
    res = pd.DataFrame(index = domains, columns = words)

    res = res[words]

    doc2vec = dict(zip(domains, vecs))
    
    for doc in doc2vec:
        res.loc[doc] = doc2vec[doc]

    return res, vectorizer
