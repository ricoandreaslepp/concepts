# recursive Euclidean algorithm 
def gcd(a, b):
    if (a==1): return "coprime"
    if (b==0): return a
    return gcd(b, a%b)

def extended_gcd():
    return None

# simple lcm
def lcm(a, b)
    return abs(a*b) // gcd(a, b)
