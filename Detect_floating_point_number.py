# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t = int(input())
check = r'^[+-.]?\d*\.\d{1,}$'
for _ in range(t):
    n = input()
    if re.match(check, n):
        print('True')
    else:
        print('False')
