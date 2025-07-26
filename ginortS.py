# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
lower = []
upper = []
odd = []
even = []
for _ in s:
    if _.islower():
        lower.append(_)
lower.sort()
for _ in s:
    if _.isupper():
        upper.append(_)
upper.sort()
for _ in s:
    if _.isdigit() and int(_) % 2 == 1:
        odd.append(_)
odd.sort()
for _ in s:
    if _.isdigit() and int(_) % 2 == 0:
        even.append(_)
even.sort()
print(''.join(map(str, lower+upper+odd+even)))
