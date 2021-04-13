import numpy as np
a=np.array([(1,2,3),(4,5,6),(7,8,9)])
b=a.ravel()
c=a[0:,2]
print(a)
print(a[0][1])
print(a.ndim)
print(a.itemsize)
print(a.size)
print(a.shape)

print(b)
b=b.reshape(9,1)
print(b)