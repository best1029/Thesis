import pandas as pd
from numpy import *

from src.dataRepresentation.mds import mds
#from src.data.goldstandard.goldstandard import goldstandard

def getBubbelChartData(model, goldstandard):

    vecs = model.vecs
    domains = model.domains
    labels_pred = model.labels

    mds_pos = mds(vecs, 2)
    x = mds_pos[:, 0]
    y = mds_pos[:, 1]

    branchen = [goldstandard[dom] for dom in domains]

    d_and_b = zip(domains, branchen)
    dom_and_branch = [val[0] + " (" + val[1] + ")" for val in d_and_b] 

    res_df = pd.DataFrame(dict(title=dom_and_branch,
                            x=x, 
                            y=y,
                            label_pred=labels_pred,
                            size = 0.5)) 
    res = res_df.as_matrix()
    res = insert(res, 0, ["title", "x", "y", "label_pred", "size"], axis = 0)
        
    return res.tolist()

def getMigrationMatrix(model, goldstandard):

    domains = model.domains
    cluster_pred = model.labels

    cluster_true = [goldstandard[dom] for dom in domains]

    res_df = pd.crosstab(pd.Series(cluster_pred), pd.Series(cluster_true))

    header = [{'label': col_header, 'type' : 'string'} for col_header in list(res_df.columns.values)]
    res = []
    res.append(header)

    values = res_df.as_matrix().tolist()

    for a in values:
        res.append(a)
    
    return res