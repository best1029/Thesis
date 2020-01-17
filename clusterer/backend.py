from src.preProcessing.stopWords import getStopWords
from src.preProcessing.preProcessing import PreProcessor

from src.dataRepresentation.vector.bagOfWords import getBOW
from src.dataRepresentation.vector.tfIdf import getTfIdf
from src.dataRepresentation.vector.embedding import Embedding

from src.algorithm.kMeans import Kmeans
from src.algorithm.hac import Hac
from src.algorithm.fuzzy import Fuzzy
from src.algorithm.optics import Optics

from src.dataRepresentation.modelRepresentation import getBubbelChartData, getMigrationMatrix
from src.evaluation.evaluation import getScores

from src.data.goldstandard.goldstandard import getGoldstandard

from src.evaluation.evaluation import *

from src.dataRepresentation.svd import svd

from src.inOut import list2file, file2list, getData
from src.logger import logger
import src.config as conf

import numpy as np
import json

class Backend:
    def __init__(self):
        self.embedding = None
        self.preProcessor = PreProcessor()
        logger.info("Preprocessor initiated")

    def loadRawData(self, depth, goldstandard, path = None, data = None):
        if data is not None:
            self.rawData = data
        elif path is not None:
            self.rawData = getData(path = path)
        else:
            self.rawData = getData(depth = depth)

        self.goldstandard = getGoldstandard(goldstandard)

        logger.info("raw Data loaded")

    def loadStopWords(self, calcStopWords = False, idf_limit = conf.default_idf_limit_min):
        self.cleanDocs = self.preProcessor.getCleanDocs(self.rawData)

        logger.info("created clean Docs for Stopword extraktion")

        if calcStopWords:
            self.stop_words = getStopWords(self.cleanDocs, idf_limit)
        else:
            self.stop_words = getStopWords()
        logger.info("Stopwords loaded")

    def getProcessedData(self, no_ppo = True, only_noun = True, stem = False, lem = False, split = False): 
        self.cleanData = self.preProcessor.text_preprocess(self.cleanDocs, self.stop_words, no_ppo = no_ppo, only_nouns=only_noun, stemming=stem, lemmatize=lem, split = split)
        return self.cleanData

    def _transformData(self, representation, n_dim, min_ngram, max_ngram, trainData = None, baseModel = "wiki"):
        df = pd.DataFrame(list(self.cleanData.items()), columns=['domain', 'content'])

        if representation == "bow":
            bow_matrix, vectorizer = getBOW(df, min_ngram, max_ngram)
            data = pd.DataFrame(list(zip(bow_matrix.index.values, bow_matrix.values)), columns = ["domain", "vec"])
        elif representation == "tfidf":
            tfidf_matrix, vectorizer = getTfIdf(df, min_ngram, max_ngram)
            data = pd.DataFrame(list(zip(tfidf_matrix.index.values, tfidf_matrix.values)), columns = ["domain", "vec"])
        elif representation == "embedding":
            if self.embedding is None:
                self.embedding = Embedding(train_data = trainData, default_model = baseModel)
            vec_dic, vectorizer = self.embedding.transform_docs2vec(df, min_ngram, max_ngram)
            data = pd.DataFrame(list(vec_dic.items()), columns = ["domain", "vec"])
        else:
            raise Exception("The representation '" + representation + "' is not supported")

        tmp = data['vec'].tolist()

        vecs = []
        for ele in tmp:
            if isinstance(ele, float) == False:
                vecs.append(ele.astype(float).tolist())

        data['vec'] = vecs

        if n_dim is not None:
            data['vec'] = svd(data['vec'].tolist(), n_dim)

        return data, vectorizer

    def runAlgorithm(self, representation, algorithm, sim, n_cluster, min_ngram, max_ngram, n_dim = None):
        data, vectorizer = self._transformData(representation, n_dim, min_ngram, max_ngram)

        logger.info("Data converted to " + representation)

        if algorithm == "Kmeans":
            model = Kmeans(data, n_cluster, vectorizer)

            #TODO -> löschen
            werte_ari = []
            werte_v = []
            samples = 1000
            for i in range(samples):
                model_bello = Kmeans(data, n_cluster, vectorizer)
                scores_borsch = getScores(model_bello, self.goldstandard)
                werte_ari.append(scores_borsch["ari"])
                werte_v.append(scores_borsch["v_measure"])
            #schnitt = sum(werte) / samples
            print("durchschnittliches ergebniss bei " + str(samples) +" durläufen:")
            #print(schnitt)

            print(werte_ari)
            print("-----------------------------------")
            print(werte_v)
            #------------------------


        elif algorithm == "HAC":
            model = Hac(data, n_cluster, similarity = sim)
        elif algorithm == "Fuzzy":
            model = Fuzzy(data, n_cluster, similarity = sim)

            #TODO -> löschen
            werte_ari = []
            werte_v = []
            samples = 1000
            for i in range(samples):
                model_bello = Fuzzy(data, n_cluster, similarity = sim)
                scores_borsch = getScores(model_bello, self.goldstandard)
                werte_ari.append(scores_borsch["ari"])
                werte_v.append(scores_borsch["v_measure"])
            #schnitt = sum(werte) / samples
            print("durchschnittliches ergebniss bei " + str(samples) +" durläufen:")
            #print(schnitt)

            print(werte_ari)
            print("-----------------------------------")
            print(werte_v)
            #------------------------

        elif algorithm == "Optics":
            model = Optics(data, similarity = sim)
        else:
            raise Exception("The algorithm '" + algorithm + "' is  not supported")
        
        logger.info("Model loaded")

        bubbleChartData = getBubbelChartData(model, self.goldstandard)
        migMa = getMigrationMatrix(model, self.goldstandard)
        scores = getScores(model, self.goldstandard)

        logger.info("Frontenddata calculated")

        res = json.dumps({"bubbleChart" : bubbleChartData, "migMa" : migMa, "scores" : scores})

        return res