import numpy as np


p = np.array(list(map(float, input().split())))
x = int(input())
print(np.polyval(p, x))
