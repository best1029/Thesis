from scipy.spatial.distance import pdist, squareform
import numpy as np

def calculate_cosine_distance(data):
    d = pdist(data, 'cosine')
    dist = 1 - d
    dist = np.nan_to_num(dist)
    return squareform(dist)