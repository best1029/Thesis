from sklearn.decomposition import TruncatedSVD
import numpy as np

def svd(data, res_dim):

    svd = TruncatedSVD(n_components=res_dim) 
    res = svd.fit_transform(data)

    return res.tolist()