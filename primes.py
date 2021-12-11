import sys
from math import sqrt

# naive
def isprime(n):
    i = 2
    while i <= sqrt(n):
        if n%i==0:
            return False
        i+=1
    return True

# ultra fast
def sieve_of_eratosthenes(n):
    is_prime = [True for _ in range(n+1)]
    
    i = 2
    while (pow(i, 2) <= n):
        
        if is_prime[i]:
            
            for j in range(pow(i, 2), n+1, i):
                is_prime[j] = False
        
        i += 1

    return list(filter(None, [i if is_prime[i] else None for i in range(2, n+1)]))

if len(sys.argv) < 2:
    print("usage: python primes.py <PRIMES_UNDER_NUMBER>")
    sys.exit(0)
    

print(*sieve_of_eratosthenes(int(sys.argv[1])))
