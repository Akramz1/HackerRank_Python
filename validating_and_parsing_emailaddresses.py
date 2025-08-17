# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
n = int(input())
for _ in range(n):
    i = input()
    i = email.utils.parseaddr(i)
    if re.match(r"^[a-zA-Z][a-zA-Z0-9\-\_\.]+@[a-z]+\.[a-z]{1,3}$", i[1]):
        print(email.utils.formataddr((i[0], i[1])))
