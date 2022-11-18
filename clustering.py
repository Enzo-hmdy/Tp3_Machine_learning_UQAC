import pandas as pd
import numpy as np

# import clustering
from sklearn.cluster import KMeans,AgglomerativeClusteringf,DBSCAN, MeanShift, SpectralClustering,AffinityPropagation, Birch,MiniBatchKMeans

# import dataset 
data = pd.read_csv('CC GENERAL.csv',delimiter=',')

data.head(5)

