'''This code loads the Fillipazo and Photometry tables and plots data after running a principle component analysis'''

import pandas as pd
import matplotlib.pyplot as plt
from PCA_adjustColumns import adjustFili, adjustPhoto
from PCA_merge import merge
from PCA_calc import distance, dm
#from PCA_index import index
from PCA_remName import remName
from PCA_impute import impute
from PCA_scale import scale
from PCA import perform
#from PCA_loadings import loadings
from PCA_plot import plot_PCA
from PCA_vectors import vectors

#load Fili Table
fili = pd.read_csv('Fili15 Table9.csv', delimiter=',')
#load Photometry Table
photo = pd.read_csv('photometry_198.csv', delimiter=',')

#adjust tables 
newfili=adjustFili(fili)
newphoto=adjustPhoto(photo)

#merge tables into one table without duplicate columns
fiPh=merge(newfili, newphoto)

#calculate distance
distance=distance(fiPh)

#return table with distance modulus accounted for  
dm=dm(distance)

newcolumns=newphoto.columns.tolist()
for elem in newcolumns:
    if elem=='shortname':
        continue
    fiPh[elem]=fiPh[elem]-dm

#remove shortname and age columns
newarray=remName(fiPh)

#impute data
data_imputed=impute(newarray)

#scale data
data_scaled=scale(data_imputed)

#fit PCA (data_scaled, # of components)
pca=perform(data_scaled, 5)

#transform PCA
data_PCA=pca.transform(data_scaled)
data_PCA=pd.DataFrame(data_PCA)

#graph PCA (x, y, z)
plot_PCA(data_PCA[0], data_PCA[1], fiPh.Gravity, data_scaled, 10, pca)

#save graph as png image
#plt.savefig('biplot3.png')
