import numpy as np
x=np.zeros([4,2])
x[0,0]=5
x[0,1]=3
x[1,0]=5.1
x[1,1]=2.5
x[2,0]=2.5
x[2,1]=4.9
x[3,0]=2.8
x[3,1]=5.2
print(x)
y=np.zeros([4,1])       # a vector
y[0]=0
y[1]=0
y[2]=1
y[3]=1
print(y)
print(y.shape)
import matplotlib.pyplot as plt
plt.plot(x[0:2,1],x[0:2,0],'ro')
plt.plot(x[2:4,1],x[2:4,0],'bo')
