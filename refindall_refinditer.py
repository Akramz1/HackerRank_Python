# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
vowels = 'AEIOUaeiou'
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
pattern = fr"(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])"
check = re.findall(pattern, s)
if check:
    for _ in check:
        print(_)
else:
    print(-1)
