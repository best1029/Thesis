import numpy as np
import gensim
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.models.word2vec import Word2Vec
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.fasttext import FastText, FastTextKeyedVectors

import src.config as conf
from src.dataRepresentation.vector.bagOfWords import getBOW
from src.dataRepresentation.vector.tfIdf import getTfIdf

import operator
from collections import Counter 

class Embedding:
    # es macht nur sinn die funktion mit train_data und default_model != wiki aufzurufen, 
    # wenn nicht schon mit train_data trainiert wurde
    def __init__(self, train_data = None, default_model = "wiki"):

        model = None

        # get pre-trained model
        if default_model == "wiki":
            model = FastText.load_fasttext_format(conf.path_model_wiki)
            model.save(conf.path_model_extended)
        elif default_model == "extended":
            raise NotImplementedError()
            #model = FastTextKeyedVectors.load(conf.pfad_model_extended)
            #model = FastText.load(conf.pfad_model_extended)
        print("model geladen")

        self.model = model

        if train_data is not None:
            self.train_further(train_data)
            print("model gespeichert")

    def train_further(self, train_data):

        # train furter with own data -> es ist unmöglich keyd vectors weiter zu trainieren
        new_data = [word_tokenize(row["content"]) for i, row in train_data.iterrows()]

        self.model.build_vocab(new_data, update=True)
        self.model.train(sentences=new_data, total_examples=len(new_data), epochs=self.model.epochs)

        print("model trained")

    def transform_docs2vec(self, df_documente, min_ngram, max_ngram, stem2word = None, base = "tfidf"):

        if base == "bow":
            word_weights, vectorizer = getBOW(df_documente, min_ngram, max_ngram)
        elif base == "tfidf":
            word_weights, vectorizer = getTfIdf(df_documente, min_ngram, max_ngram)
        else:
            raise Exception("The representation '" + base + "' is  not supported")
        
        print("abd")
        print(word_weights)
        print(type(word_weights))

        words = word_weights.columns.tolist()
        vecs = {}    

        for domain, weights in word_weights.iterrows():
            vec = None
            for word in words:
                if vec is not None:
                    vec += self.model[word] * weights[word]   
                else:
                    vec = self.model[word] * weights[word]
            vecs[domain] = vec
        
        return vecs

    