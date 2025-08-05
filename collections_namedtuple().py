from collections import namedtuple
N, Student = int(input()), namedtuple('Student', input().split())
print(sum([int(Student(*input().split()).MARKS) for _ in range(N)])/N)
