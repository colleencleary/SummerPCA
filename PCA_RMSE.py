'''This function returns the RMSE'''
import numpy as np

def RMSE(y,pred_y):
    return np.sqrt(((y-pred_y)**2).mean())
