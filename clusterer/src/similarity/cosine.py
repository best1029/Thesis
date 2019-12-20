from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_distance(data):
    dist = 1 - cosine_similarity(data)

    print(type(dist))
    
    return dist