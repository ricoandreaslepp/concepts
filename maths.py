# recursive Euclidean algorithm 
def gcd(a, b):
    if (a==1): return "coprime"
    if (b==0): return a
    return gcd(b, a%b)

# pu + qv = gcd(p, q)
# pu + qv = 1 # take modulo q both sides
# pu + qv = 1 (mod q) # qv (mod q) is always 0
# pu ~ 1 (mod q) # which is modular inverse

# Extended gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# simple lcm
def lcm(a, b)
    return abs(a*b) // gcd(a, b)
