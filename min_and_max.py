import numpy as np

n, m = map(int, (input()).split())
nums = np.array([list(map(int, (input()).split())) for _ in range(n)])
print(np.max(np.min(nums, axis=1)))
