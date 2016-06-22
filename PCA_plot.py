import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

def plot_PCA(x_value, y_value, z_value, data_scaled, factor, pca, loadings, save):
    plt.scatter(x_value, y_value, c=z_value)
    #plt.ylim([-4,4])
    #plt.xlim([-4,4])
    #plt.title('PCA of Star Data')
    
     
    plt.colorbar().set_label(z_value.name)
    plt.xlabel(x_value.name)
    plt.ylabel(y_value.name)
    plt.gca().invert_yaxis()
    
    if loadings==1:
        loadings=pd.DataFrame(pca.components_,columns=data_scaled.columns.tolist())
        loadings_sq=loadings**2
        loadings_sq=loadings_sq.transpose()
    
        plt.arrow(0,0,loadings.Temperature[x_value.name]*factor, loadings.Temperature[y_value.name]*factor, color='red')
        plt.arrow(0,0,loadings.Luminosity[x_value.name]*factor, loadings.Luminosity[y_value.name]*factor, color='blue')
        plt.arrow(0,0, loadings.Gravity[x_value.name]*factor, loadings.Gravity[y_value.name]*factor, color='green')
        plt.text(loadings.Temperature[x_value.name]*factor, loadings.Temperature[y_value.name]*factor, 'Temperature', color='red')
        plt.text(loadings.Luminosity[x_value.name]*factor, loadings.Luminosity[y_value.name]*factor, 'Luminosity', color='blue')
        plt.text(loadings.Gravity[x_value.name]*factor, loadings.Gravity[y_value.name]*factor, 'Gravity', color='green')
    else: pass
    if save==1:
        plt.savefig('/Users/Owner/Summer_Research/graphs/'+x_value.name+'_'+y_value.name+'_'+z_value.name+'.png') 
    else: pass
    plt.show()

