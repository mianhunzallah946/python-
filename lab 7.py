#matrices
import numpy as np
m=np.array([[10,20,30],[40,50,60],[70,80,90]])

print(m.shape)
print(m.ndim )

print(m[1,1])
print(m[1])
print(m[2])
#mean
mmean=np.mean(m)
print(mmean)
axismean=np.mean(m,axis=0)
print(axismean)
