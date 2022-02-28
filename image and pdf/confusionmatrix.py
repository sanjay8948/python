import numpy as np
def gen_confusion_matrix(X,Y,N):
    """
    Inputs:
        Yactual: numpy array of shape (samples, ) with actual output values
        Ypredicted: numpy array of shape (samples, ) with predicted output values
        Ny: number of unique output classes
    Outputs:
        cm: numpy array of shape (Ny, Ny) containing confusion matrix 
    """
    ### Your code here
    A=np.zeros((2,2))
    j=0.5
    while j<=N:
        for i in range(len(Y)):
            if int(X[i])==1:
                if float(Y[i])<j:
                    A[0][1]=A[0][1]+1
                else:
                    A[0][0]=A[0][0]+1
            elif int(X[i]==0):
                if float(Y[i])>j:
                    A[1][0]=A[1][0]+1
                else:
                    A[1][1]=A[1][1]+1
        j=j+1
    return A
  
  
x=np.array([1,1,0,0,1,0,0,1,1,1,1,0])
y=np.array([1,0,0,1,0,0,1,1,1,1,0,0])

print(gen_confusion_matrix(x,y,3))
  
