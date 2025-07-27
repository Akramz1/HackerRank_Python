# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby


s = input()
ans = []
for num, count in groupby(s):
    ans.append(f'({len(list(count))}, {num})')
print(' '.join(ans))
