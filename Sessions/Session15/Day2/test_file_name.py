import numpy as np
from sklearn.neighbors import NearestNeighbors
from file_name import *

def test_distance():
    # complete
    X = np.array([[1,1], [3,3]])
        
    d = np.sqrt( (X[0, 0]-X[1,0])**2 + 
                          (X[0, 1]-X[1,1])**2)
    dis = [d,d]
    assert dis[0] == distance(X)[0]

def test_average():
    X=[1,2]
    avg = np.sum(X)/len(X)
    assert avg == average(X)

def test_minimum():
    X=[3,4,-1]
    assert -1 == minimum(X)
    
def test_maximum():
    X=[3,4,-1]
    assert 4 == maximum(X)
