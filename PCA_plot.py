import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

def plot_PCA(data_PCA, y_value, z_value, data_scaled, factor, pca):
    plt.scatter(data_PCA, y_value, c=z_value)
    #plt.ylim([-4,4])
    plt.xlim([-2,-8])
    plt.title('PCA of Star Data')
    plt.colorbar().set_label('Gravity')
    plt.xlabel('PCA[0]')
    plt.ylabel('PCA[3]')
    
    loadings=pd.DataFrame(pca.components_,columns=data_scaled.columns.tolist())
    loadings_sq=loadings**2
    loadings_sq=loadings_sq.transpose()

    plt.arrow(0,0,loadings.Temperature[0]*factor, loadings.Temperature[3]*factor, color='red')
    plt.arrow(0,0,loadings.Luminosity[0]*factor, loadings.Luminosity[3]*factor, color='blue')
    plt.arrow(0,0, loadings.Gravity[0]*factor, loadings.Gravity[3]*factor, color='green')
    plt.text(loadings.Temperature[0]*factor, loadings.Temperature[3]*factor, 'Temperature', color='red')
    plt.text(loadings.Luminosity[0]*factor, loadings.Luminosity[3]*factor, 'Luminosity', color='blue')
    plt.text(loadings.Gravity[0]*factor, loadings.Gravity[3]*factor, 'Gravity', color='green')

    plt.show()

