# HackerRank Fibonacci Finding (easy) solution

def matrix_mult(x, y=None, v=None):
    global mod

    # for first binary
    if x==None:
        return y
    
    # for last vector multiplication
    if v!=None:
        a = x[0]*v[0] + x[1]*v[1]
        b = x[2]*v[0] + x[3]*v[1]
        return [a%mod, b%mod]
        
    a = x[0]*y[0] + x[1]*y[2]
    b = x[0]*y[1] + x[1]*y[3]
    c = x[2]*y[0] + x[3]*y[2]
    d = x[2]*y[1] + x[3]*y[3]

    return [a%mod, b%mod, c%mod, d%mod]

def binary_expo(n):
    B = [0, 1, 1, 1]
    res = None
    
    while (n > 0):

        if n%2==1:
            res = matrix_mult(res, B)

        n >>= 1
        B = matrix_mult(B, B)

    return res

def solve(a, b, n):
    global mod
    
    v = [a, b]

    # edge cases
    if n==1:
        return b
    elif n==0:
        return a

    resn = binary_expo(n)
    
    return int((matrix_mult(resn, v=v)[0]) % mod)

# must be int, cause float will cause round errors on higher values
mod = int(1e9+7)

cases = int(input())
for _ in range(cases):
    # f(0), f(1), n-th fibonacci number
    a, b, n = list(map(int, input().split(" ")))
    print(solve(a, b, n))


