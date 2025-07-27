# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())
a = []
for _ in range(x):
    a.append(list(map(float, input().split())))
for _ in list(zip(*(a))):
    print(sum(_)/x)
