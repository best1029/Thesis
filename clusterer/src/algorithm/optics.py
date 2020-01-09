from sklearn.cluster import OPTICS
import numpy as np

from src.dataRepresentation.modelRepresentation import getBubbelChartData, getMigrationMatrix
from src.evaluation.evaluation import getScores

class Optics:
    def __init__(self, data, similarity):
        vecs = data['vec'].tolist()

        optics_model = OPTICS(min_samples = 5, metric = similarity)
        optics_model.fit(vecs)
   
        self.model = optics_model
        self.data = data

        self.domains = data['domain'].tolist()
        self.vecs = data['vec'].tolist()
        self.labels = self.model.labels_.tolist()

    def getFrontendScores(self):
        return getScores(self.domains, self.labels)

    def getFrontendBubbelChartData(self):
        return getBubbelChartData(self.vecs,  self.domains, self.labels)

    def getFrontendMigrationMatrix(self):
        return getMigrationMatrix(self.domains, self.labels)