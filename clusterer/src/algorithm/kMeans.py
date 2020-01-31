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