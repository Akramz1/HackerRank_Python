import numpy as np

n, m = map(int, (input()).split())
nums = np.array([list(map(int, (input()).split())) for _ in range(n)])
print(f'{np.mean(nums, axis=1)}\n{np.var(nums, axis=0)}\n{round(np.std(nums), 11)}')
