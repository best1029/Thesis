from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

def getBOW(df_documente, min_ngram, max_ngram, typ="relativ"):
    content = df_documente["content"]
    domains = df_documente["domain"]

    vectorizer = CountVectorizer(ngram_range=(min_ngram, max_ngram))
    matrix = vectorizer.fit_transform(content) 
    vecs = matrix.toarray()
    
    words = vectorizer.get_feature_names()
    
    res = pd.DataFrame(index = domains, columns = words)
        
    if typ == "relativ":
        all_vecs = []
        for vec in vecs:
            num_words = sum(vec)
            tmp_vec = [occurence/num_words for occurence in vec]
            all_vecs.append(tmp_vec)
        doc2vec = dict(zip(domains, all_vecs))
    elif typ == "absolute":
        doc2vec = dict(zip(domains, vecs))
    else:
        raise Exception("'" + typ + "' wird nicht unterstützt")
        
    for doc in doc2vec:
        res.loc[doc] = doc2vec[doc]

    return res, vectorizer

