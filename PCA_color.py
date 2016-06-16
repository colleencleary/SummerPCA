
def colorColumns(newfiPh):
    '''This function returns an array containing color values'''
    colnames=newfiPh.columns.tolist()
    #colnames=colnames[6:]
    
    for band in colnames[6:] :
        for i in colnames[6:] :
            if i not in band :
                newcol = band + '-' + i
                newfiPh[newcol]=newfiPh[band]-newfiPh.i
            else :
                pass

    return newfiPh