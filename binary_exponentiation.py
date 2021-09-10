def bin_exp(a, b):
    ans = 1
    
    while (b > 0):

        if b%2==1:
            ans *= a

        b >>= 1
        a *= a

    return ans

def rec_bin_exp(a, b):
    #TO-DO
    return None

def dif_bin_exp(a, b):
    # I wrote this version
    # just to clearify to myself
    # what binary exponentiation really is
    # when broken down to the very lowest levels
    ans = 1
    
    for i in list(map(int, bin(b)[2:][::-1])):

        if (i==1):
            ans *= a

        a *= a
        
    return ans
