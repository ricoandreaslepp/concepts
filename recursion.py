# Pairs of functions for explaining the value of dp contrasted with recursion

from time import time
import sys

sys.setrecursionlimit(2500)

# ----------------------------------------
# The Fibonacci Sequence
# ----------------------------------------
def run_Fibonacci():
    print("Running recursive Fibonacci functions...")

    N = 31

    cnt = 0
    def fib(n): # recursive and naive
        if n==0: return 0
        if n==1: return 1
        return fib(n-1)+fib(n-2)

    start = time()
    print(fib(N))
    print(f"fib(n) took {time()-start} seconds")

    # ----------------------------------------

    start = time()
    s = [0, 1]
    def dp(n): # recursive with dynamic memoization
        if n==0: return s[0]
        if n==1: return s[1]
        if n >= len(s):
            s.append(dp(n-1)+dp(n-2))
        return s[n]

    print(dp(N))
    print(f"dp(n) took {time()-start} seconds")
    print()

#run_Fibonacci()

# ----------------------------------------
# The 0-1 Knapsack Problem
# ----------------------------------------
def run_Knapsack_Problem():
    print("Running recursive Knapsack Problem solutions...")
    print("First 2 functions should have similar (-ly slow) run times.")

    global ans, max_cap
    from random import randint
    w = [randint(1, 1000) for i in range(1000)]
    v = [randint(1, 200) for i in range(1000)]
    max_cap = 40

    ans = 0
    def grec_ks(p, val, capacity_left): # similar recursion but with global storage, easier to grasp
        global ans

        if p==len(v):
            ans = max(ans, val)
        elif capacity_left-w[p] < 0:
            return grec_ks(p+1, val, capacity_left)
        else:
            grec_ks(p+1, val+v[p], capacity_left-w[p]) # include
            grec_ks(p+1, val, capacity_left) # don't
        return ans

    start = time()
    print(grec_ks(0, 0, max_cap))
    print(f"grec_ks(n) took {time()-start} seconds")
    print()

    # ----------------------------------------

    def rec_ks(p, capacity_left): # recursion with local storage - more pythonic, but harder to grasp

        if p == len(v):
            ans = 0
        elif w[p] > capacity_left:
            ans = rec_ks(p+1, capacity_left)
        else:
            a = rec_ks(p+1, capacity_left) # don't include item
            b = v[p] + rec_ks(p+1, capacity_left-w[p]) # include the item
            ans = max(a, b)
        return ans

    start = time()
    print(rec_ks(0, max_cap))
    print(f"rec_ks(n) took {time()-start} seconds")
    print()

    # 2D array of p*capacity_left
    s = [[None]*(max_cap+1) for _ in range(len(v)+1)]

    # more items = more stored
    def rec_dp_ks(p, capacity_left):
        if s[p][capacity_left] != None:
            return s[p][capacity_left]
        
        if p == len(v):
            ans = 0
        elif w[p] > capacity_left:
            ans = rec_dp_ks(p+1, capacity_left)
        else:
            a = rec_dp_ks(p+1, capacity_left) # don't include item
            b = v[p] + rec_dp_ks(p+1, capacity_left-w[p]) # include the item
            ans = max(a, b)

        s[p][capacity_left] = ans
        return ans

    start = time()
    print(rec_dp_ks(0, max_cap))
    print(f"rec_dp_ks(n) took {time()-start} seconds")
    print()
            

#run_Knapsack_Problem()
