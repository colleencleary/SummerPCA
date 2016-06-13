import pandas as pd
from sklearn.decomposition import PCA

def perform(data_scaled, components):
    '''This function performs a principal component analysis on the given array'''
    pca=PCA(n_components=components)
    pca.fit(data_scaled)
    return pca

