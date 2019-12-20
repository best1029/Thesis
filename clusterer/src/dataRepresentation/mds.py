from sklearn.manifold import MDS

def mds(data, res_dim):
    mds = MDS(n_components=res_dim, random_state=1) 
    pos = mds.fit_transform(data)
    
    return pos