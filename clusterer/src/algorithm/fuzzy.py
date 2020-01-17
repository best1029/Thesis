import skfuzzy as fuzz
import numpy as np

from src.dataRepresentation.modelRepresentation import getBubbelChartData, getMigrationMatrix
from src.evaluation.evaluation import getScores
from src.dataRepresentation.svd import svd

class Fuzzy:
    def __init__(self, data, n_clu, similarity, fuzzy_tolerance = 0.3):

        vecs = data['vec'].tolist() 

        alldata = np.transpose(vecs)
        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(alldata, n_clu, 2, error=0.005, maxiter=1000, init=None, metric = similarity)
        self.data = data

        self.domains = data['domain'].tolist()
        self.vecs = data['vec'].tolist()

        u_trans = np.transpose(u)

        self.labels = np.argmax(u, axis=0)
        # print(self.labels)

        # self.labels = []
        # for a in u_trans:
        #     if np.amax(a) >= fuzzy_tolerance:
        #         self.labels.append(np.argmax(a))
        #     else:
        #         self.labels.append(10 * n_clu)