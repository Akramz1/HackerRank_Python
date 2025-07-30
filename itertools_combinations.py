# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s = input().split()
n, m = sorted(s[0]), int(s[1])
ans = []

for _ in range(1, m+1):
    comb = list(combinations(n, _))
    ans.extend(comb)

for _ in ans:
    print(''.join(_))
