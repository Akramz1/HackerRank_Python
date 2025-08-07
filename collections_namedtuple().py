# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
lo = input().split()
it = namedtuple('student', lo)
students = []
total = 0
for _ in range(n):
    s = input().split()
    student = it(*s)
    students.append(student)
    num = int(student.MARKS)
    total += num
print(total/len(students))
