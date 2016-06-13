import numpy as np

def distance(fiPh):
    '''This function returns the distance'''
    return 1000/fiPh.Parallax

def dm(distance):
    '''This function returns the distance modulus''' 
    return 5*np.log10(distance)-5
    
    
