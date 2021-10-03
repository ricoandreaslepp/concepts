## some implementations of different types of edit distances or Levenshtein distances

from collections import deque
def find_distance_path(a, b):
    ## MODIFIED
    # slower version, but can save all the operations
    # distance to get from a to b with operations on a:
    # 1) erase ANY digit
    # 2) add one digit to the right
    
    a, b = deque(a), deque(b)
    
    popped = i = j = 0
    while i<len(a) and j<len(b):
        
        if b[i]==a[j]:
            print(f"common element at {j}")
            j += 1
            i += 1
        else:
            print(f"remove element at {j} from {a}")
            a.remove(a[j])
            popped += 1
    
    
    if a==b:
        return popped
    else:
        print(f"adding the ending of {b} to {a}")
        return popped+abs(len(b)-len(a))
      
def find_distance(a, b):
    ## MODIFIED
    # faster version of find_distance_path(), without saving the path
    popped = i = j = 0
    while i<len(b) and j<len(a):
        
        if b[i]==a[j]:
            i+=1
        else:
            popped += 1
        
        j+=1
    
    # popped every item that wasn't in the substring
    return abs(len(b)-len(a)+popped)+popped
      
# return a distance list to make integer a power of 2
def make_power_of_two(a):
    pows = list(pow(2, x) for x in range(61)) # pows of 2 under 10^18
    return list(map(lambda x: find_distance(x[0], x[1]), list([a, str(x)] for x in pows)))

print("Find edit distance from A to B with the following actions:")
print(" * erase ANY character from A")
print(" * add one character to the right of A")

for _ in range(1000):
    print()
    a = input("string A -> ")
    b = input("string B -> ")
    print("-"*15)
    print("running algorithm...")
    print(f'it takes {find_distance_path(a, b)} steps to make "{a}" into "{b}"')
