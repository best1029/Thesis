from sklearn.cluster import AgglomerativeClustering

from src.dataRepresentation.modelRepresentation import getBubbelChartData, getMigrationMatrix
from src.evaluation.evaluation import getScores
from src.logger import logger
from src.similarity.cosine import calculate_cosine_distance
from src.similarity.jaccard import calculate_jaccard_similarity

class Hac:
    def __init__(self, data, n_clu, vectorizer, similarity):
        
        link = "ward"
        cluster_data = data['vec'].tolist()

        if similarity != 'euclidean':
            link = "average"
            if similarity == 'cosine':
                precomputed_dist = calculate_cosine_distance(cluster_data)
            elif similarity == 'jaccard':
                precomputed_dist = calculate_jaccard_similarity(cluster_data)
            else:
                raise Exception(similarity + " wird nicht unterstützt")
            similarity = 'precomputed'
            cluster_data = precomputed_dist

        hac_model = AgglomerativeClustering(n_clusters = n_clu, affinity = similarity, linkage = link)
        hac_model.fit(cluster_data)  

        self.model = hac_model
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