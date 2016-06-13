import pandas as pd
from sklearn.preprocessing import Imputer

def impute(newarray):
    '''This function performs imputation on the newarray data'''
    imp=Imputer(strategy="mean")
    imp.fit(newarray)
    data_imputed=imp.transform(newarray)
    return pd.DataFrame(data_imputed,columns=newarray.columns.tolist())
