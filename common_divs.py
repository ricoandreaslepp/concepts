from math import sqrt

# find divisors in O(sqrt(N)) instead of O(N)

divs = []
n = int(input())
i = 1
while i <= sqrt(n):

    if n % i == 0:
        divs.append(i)
        if n // i != i:
            divs.append(n//i)

    i += 1

print(*divs)
