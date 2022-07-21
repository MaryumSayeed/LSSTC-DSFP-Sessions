import numpy as np
from sklearn.neighbors import NearestNeighbors

def distance(data):
    '''Returns distances between clusters.'''
    neigh = NearestNeighbors(n_neighbors=2)
    nbrs = neigh.fit(data)
    distances, indices = nbrs.kneighbors(data)
    return distances[:,1]

def average(distances):
    '''Returns average cluster distance.'''
    return np.nanmean(distances)

def minimum(distances):
    '''Returns minimum cluster distance.'''
    return np.nanmin(distances)

def maximum(distances):
    '''Returns maximum cluster distance.'''
    return np.nanmax(distances)