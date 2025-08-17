# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    s = input()
    if len(s) == 10 and s[0] in ['7', '8', '9'] and s.isdigit():
        print("YES")
    else:
        print("NO")
