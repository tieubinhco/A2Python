import matplotlib.pyplot as plt
import numpy as np
check = np.zeros((8, 8))
check[::2, 1::2] = 1
check[1::2, ::2] = 1
c = plt.imshow(check, cmap='gray', interpolation='nearest')
plt.colorbar(c)
plt.show()
