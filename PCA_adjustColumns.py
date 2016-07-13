'''This code optimizes the columns:
1) Columns are renamed
2) Reference/Uncertainty columns are removed 
3)Columns with up to 50% null values are removed.'''

import numpy as np

def adjustFili(fili):
    '''This code returns the Filipazzo table without uncertainty/reference columns'''
#rename columns
    cols = fili.columns.tolist()
    cols[1] = 'Parallax'
    cols[2] = 'Parallax(Uncertainty)'
    cols[4] = 'Luminosity'
    cols[5] = 'Luminosity(Uncertainty)'
    cols[6] = 'Age'
    cols[7] = 'Radius'
    cols[8] = 'Radius(Uncertainty)'
    cols[9] = 'Gravity'
    cols[10] = 'Gravity(Uncertainty)'
    cols[11] = 'Temperature'
    cols[12] = 'Temperature(Uncertainty)'
    cols[13] = 'Mass'
    cols[14] = 'Mass(Uncertainty)'

#names of columns!
    fili.columns = cols
    
#remove uncertainty and ref columns
    refColumns=[col for col in fili.columns if 'pi_ref' not in col]
    newfili=fili[refColumns].copy()
    uncColumns=[col for col in newfili.columns if 'Uncertainty' not in col]
    newfili=newfili[uncColumns].copy()

    return newfili

def adjustPhoto(photo):
    '''This returns the photo file without columns that are mostly null values'''
    nullValues=photo.isnull().sum()
    keepcol=np.where(nullValues<len(photo)*0.5)[0]
    newphoto=photo[keepcol].copy()
    
    return newphoto
