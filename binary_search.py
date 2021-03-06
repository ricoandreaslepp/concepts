# to-do
def binary_search():
    return None

# recursive approach
import sys
sys.setrecursionlimit(10000)
def binSearch(arr, start, end, x):
    
    if end >= start:
        
        mid = start + (end-start) // 2
    
        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            # check the lower half
            return binSearch(arr, start, mid-1, x)
        else:
            # check the upper half
            return binSearch(arr, mid+1, end, x)
    else:
        return f"[-] integer not in sequence\n[+] but would fit between indices {end} and {start}"


# has to be a sorted list
a = [1, 3, 4, 5, 6, 12]

for _ in range(15):
    x = int(input("Enter int to find: "))
    print(binSearch(a, 0, len(a)-1, x))
        
