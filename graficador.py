import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

vec=np.loadtxt('filename.txt',usecols=0)

Z=np.zeros(shape=(100,100))

    
for i in range(100):
    Z[i,:]=vec[i*100:(i+1)*100]
    
X=np.array(range(100))
Y=X
X,Y=np.meshgrid(X,Y)
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_wireframe(X,Y,Z, color='r')
plt.savefig('graficas.png')