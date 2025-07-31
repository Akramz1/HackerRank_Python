import numpy as np


n = int(input())
a = np.array([list(map(float, input().split())) for _ in range(n)])
print(round(np.linalg.det(a), 2))
