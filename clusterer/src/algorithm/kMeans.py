from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

from src.dataRepresentation.modelRepresentation import getBubbelChartData, getMigrationMatrix
from src.evaluation.evaluation import getScores

class Kmeans:
    def __init__(self, data, n_clu, vectorizer):
        vecs = data['vec'].tolist()

        kmeans_model = KMeans(n_clusters = n_clu) 
        kmeans_model.fit(vecs)    
        self.model = kmeans_model
        self.data = data

        self.domains = data['domain'].tolist()
        self.vecs = data['vec'].tolist()
        self.labels = self.model.labels_.tolist()

        order_centroids = self.model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()

        for i in range(n_clu):
            print("Cluster %d:" % i),
            for ind in order_centroids[i, :10]:
                print(' %s' % terms[ind])

    def getFrontendScores(self):
        return getScores(self.domains, self.labels)

    def getFrontendBubbelChartData(self):
        return getBubbelChartData(self.vecs,  self.domains, self.labels)

    def getFrontendMigrationMatrix(self):
        return getMigrationMatrix(self.domains, self.labels)