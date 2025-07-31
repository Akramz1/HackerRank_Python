# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

ip = input().split()
s, k = sorted(ip[0]), int(ip[1])
ans = []
for _ in range(1, k+1):
    comb = list(combinations_with_replacement(s, _))
    ans.extend(comb)

for _ in comb:
    print(''.join(_))
