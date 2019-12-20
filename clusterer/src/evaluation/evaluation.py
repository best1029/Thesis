import json
import pandas as pd
from sklearn.metrics.cluster import adjusted_rand_score, homogeneity_score, completeness_score, v_measure_score
from sklearn.metrics import accuracy_score

from src.data.goldstandard.goldstandard import goldstandard

def getScores(domains, cluster_pred):

    cluster_true = [goldstandard[dom] for dom in domains]
    res = {}

    res["ari"] = adjusted_rand_score(cluster_true, cluster_pred)
    res["homo_score"] = homogeneity_score(cluster_true, cluster_pred)
    res["completness"] = completeness_score(cluster_true, cluster_pred)
    res["v_measure"] = v_measure_score(cluster_true, cluster_pred)

    return res
