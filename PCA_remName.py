
def remName(fiPh):
    '''This function creates a new array that stores a version of fiPh without the name and age columns'''
    return fiPh.drop(["shortname","Age"], axis=1).copy()
