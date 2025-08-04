# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n , m = map(int, input().split())
mid = math.floor(n/2)
for i in range(0 ,mid):
    print(('.|.'*(i*2+1)).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(mid-1,-1,-1):
    print(('.|.'*(i*2+1)).center(m,'-'))