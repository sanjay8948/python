import numpy as np

def createA(x,D):
    N=x.shape[0]
    A=np.ones((N,D+1))
    for d in range(1,D+1):
        A[:,d]=np.power(x,d)
    return A    
    


x=np.array([2,4,6])
print(createA(x,2))

