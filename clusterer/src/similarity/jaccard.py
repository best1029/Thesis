from scipy.spatial.distance import pdist, squareform

def calculate_jaccard_similarity(data):
    d = pdist(data, 'jaccard')
    dist = 1 - d

    return squareform(dist)