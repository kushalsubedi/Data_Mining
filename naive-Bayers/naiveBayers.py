import numpy as np 


DATA = [ 
    # fever, cough, headache, runny nose, flu,  Covid-19
   [ 1, 1, 0, 0, 1, 0],
   [ 0, 1, 1, 0, 1, 0],

    [ 1, 0, 0, 1, 0, 1],
    [ 0, 0, 1, 1, 0, 1],
    [ 1, 1, 1, 1, 0, 1],
    [ 1, 1, 1, 1, 1,0],
    [ 0, 0, 0, 0, 0, 0],
    [ 1, 0, 1, 0, 1, 0],
    [ 0, 1, 0, 1, 0, 1],
    [ 1, 0, 1, 1, 0, 1]


]
def get_Features(data):
    return np.array(data)[:,0:4]

def get_Target(data):
    return np.array(data)[:,4:6]


def naiveBayers (data,target):
    pass 



print (get_Features(DATA))
print (get_Target(DATA)) #flu, covid-19