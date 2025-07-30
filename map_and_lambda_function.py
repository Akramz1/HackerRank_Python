def cube(x): return x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    if n == 1:
        return [0]
    nums = []
    a, b = 0, 1
    nums.append(a)
    nums.append(b)
    for _ in range(n-2):
        a, b = b, a+b
        nums.append(b)
    return nums


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
