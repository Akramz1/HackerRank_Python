# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
res = re.search(r'([a-zA-Z0-9])\1', s)
if res:
    print(res.group())
else:
    print('-1')
