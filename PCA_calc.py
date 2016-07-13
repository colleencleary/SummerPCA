import numpy as np

def calc_distance(fiPh):
    '''This function returns the distance'''
    return 1000/fiPh.Parallax

def calc_dm(distance):
    '''This function returns the distance modulus''' 
    return 5*np.log10(distance)-5
    
    
