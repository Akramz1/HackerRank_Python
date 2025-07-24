import numpy as np

np.set_printoptions(legacy='1.13')
nums = np.array(list(map(float, (input()).split())))
print(np.floor(nums))
print(np.ceil(nums))
print(np.rint(nums))
