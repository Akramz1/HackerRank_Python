# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = [input() for i in range(n)]
res = {}
for _ in words:
    if _ not in res:
        res[_] = 1
    else:
        res[_] += 1
print(len(res))
for _ in res.values():
    print(_, end=" ")
