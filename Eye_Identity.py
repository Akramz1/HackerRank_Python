import numpy as np
np.set_printoptions(legacy='1.13')


n1, n2 = map(int, (input()).split())
print(np.eye(n1, n2))
