# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
pattern = r'(\#[0-9a-fA-F]{3,6})(;|,|.;)'
s = ""
for _ in range(n):
    s = s+''.join(input())

matches = re.findall(pattern, s)
for match in matches:
    print(match[0])
