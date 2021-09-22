from math import sqrt

# find divisors in O(sqrt(N)) instead of O(N)
# ------------------------------------------
# lies on the idea that any non-prime number
# can be expressed as: a*b (where 1 < a <=b)
# if a = b (n//i==i) then we don't count it twice
# otherwise we've found another divisor

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
