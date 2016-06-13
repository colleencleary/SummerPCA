import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale(data_imputed):
    '''This function returns the data scaled'''
    scaler=StandardScaler()
    data_scaled=scaler.fit_transform(data_imputed)
    return pd.DataFrame(data_scaled,columns=data_imputed.columns.tolist())
