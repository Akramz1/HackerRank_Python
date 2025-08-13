# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()
m = re.search(k, s)
flag = False
for _ in re.finditer(rf'(?=({k}))', s):
    print((_.start(1), _.end(1)-1))
    flag = True
if not flag:
    print((-1, -1))
