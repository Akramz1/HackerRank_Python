# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
ordered_dic = OrderedDict()
for _ in range(n):
    s = input().split()
    if ' '.join(s[0:len(s)-1:]) in ordered_dic:
        ordered_dic[' '.join(s[0:len(s)-1:])] += int(s[-1])
    else:
        ordered_dic[' '.join(s[0:len(s)-1:])] = int(s[-1])
for item, price in ordered_dic.items():
    print(item, price)
