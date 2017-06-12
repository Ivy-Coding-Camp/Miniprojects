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


def print_pascals_triangle(k):
    r=0
    while r < k:
        row = pascals_row(r)
        for i in range(len(row)):
            print(row[i], end=' ')
        print()
        r += 1

def pascals_row(r):
    i=0
    row = list()
    while i <= r:
        row.append(combination(r,i))
        i += 1
    return row

while True:
    try:
        k = int(input("Enter number of rows for Pascals Triangle: "))
        print_pascals_triangle(k)
    except:
        print("Bye!")
        break