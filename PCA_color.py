
def colorColumns(newfiPh, BDdict):
    '''This function returns an array containing color values'''
  
    colnames=newfiPh.columns.tolist()
    #colnames=colnames[6:]
    
    for band in colnames[6:] :
        for n in colnames[6:] :
            if BDdict[band] < BDdict[n] :
                    newcol = band + '-' + n
                    newfiPh[newcol]=newfiPh[band]-newfiPh[n]               
            

    return newfiPh