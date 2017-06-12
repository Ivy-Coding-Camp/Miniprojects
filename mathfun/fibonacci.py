def fib(n):
    a, b = 0, 1
    i=0
    while i < n:
        print(b, end=' ')
        a, b = b, a + b
        i += 1
    print()


print(fib(10))