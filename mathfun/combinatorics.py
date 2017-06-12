from __future__ import print_function


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def permutation(n, r):
    return factorial(n) / factorial(n - r)


def combination(n, r):
    return permutation(n,r)/factorial(r)


while True:
    try:
        n = int(input("Provide a positive number for n: "))

        if n < 0:
            print("The value of n should be positive. Try again...")
            continue

        r = int(input("Provide a positive number for r : "))

        if r < 0 or n < r:
            print("The value of r should be positive and less than or equal to n. Try again...")
            continue

        print("The value of ", n, "P", r, " = ", permutation(n,r))
        print("The value of ", n, "C", r, " = ", combination(n,r))
    except:
        print("Bye!")
        break



