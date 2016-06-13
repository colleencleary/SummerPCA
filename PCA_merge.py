import pandas as pd

def merge(newfili, newphoto):
    '''This function returns a new table composed of newfili and newphoto merged'''
#merge tables
    fiPh = pd.merge(newfili, newphoto, how='outer', on=['shortname', 'shortname'])
    
    return fiPh
