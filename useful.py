"""
###

A few very useful methods/data structures to use in Python


### MATERIALS
* https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/
* https://www.section.io/engineering-education/graph-data-structure-python/
* https://www.reddit.com/r/Python/comments/73kw2c/python_for_competitive_coding_data_structures_and/
* https://www.geeksforgeeks.org/python-tricks-competitive-coding/
* https://codeforces.com/blog/entry/80317
* https://docs.python.org/3/library/itertools.html

### SPECIFIC
* https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
* https://headbreakz.tistory.com/entry/Code-Python-heapq-deque

"""

def next():
    print("\n"*2)
### ------------------------------------------------------------------------------------- ###
### maintain a list in sorted order without having to sort the list after each insertion. ###
# For long lists of items with expensive comparison operations, this can be an improvement over the more common approach.
# Uses a basic bisection algorithm
# more useful methods -> insort
import bisect
a = [1, 2, 3, 5, 6, 7]

### ------------------------------------------------------------------------------------- ###
### Generate combinations and permutations
from itertools import combinations, permutations

a = [1,2,3,4]
print(list(combinations(a, 2)))
print(list(permutations(a, 2)))

### ------------------------------------------------------------------------------------- ###
### Heap Queue algorithm in Python

# A heap has two variants:
# 1) max-heap, parent is more than or equal to both of its child nodes
# 2) min-heap, parent is smaller or equal to child nodes

# supports addition and removal of the smallest element in O(log n) time
# each time the smallest element is popped, maintains structure
# with each push or pop.
import heapq
# heapify converts the iterable into a heap (ds)
a = [5, 7, 9, 1, 3]
heapq.heapify(a)
print(f"heapq: {a}")

# inserts the elements, adjusts order to maintain the heap structure
heapq.heappush(a, 4)
print(f"heapq after pushing element 4: {a}")

# largest and smallest elements
print(f"2 biggest: {heapq.nlargest(2, a)}")
print(f"2 smallest: {heapq.nsmallest(2, a)}")

# pops the smallest element, adjusts the structure accordingly
a = [1,2,3,4]
heapq.heapify(a)
print(f"2 first pops from min heap {heapq.heappop(a), heapq.heappop(a)}")

# max heap quick implementation
a = [-i for i in a]
heapq.heapify(a)
print(f"2 first pops from max heap {-heapq.heappop(a), -heapq.heappop(a)}")

next()
### ------------------------------------------------------------------------------------- ###
### extremely useful for rotation or left-right insertion/removals
# more useful methods -> pop, insert, extend
from collections import deque
a = deque(x for x in range(1, 6))
print(f"{a}")
a.rotate(-1)
print(f"after 1 backshift -> {a}")
a.rotate(3)
print(f"after 3 rightshifts -> {a}")
a.append(7)
print(f"after appending 7 -> {a}")
a.appendleft(9)
print(f"after prepending 9 -> {a}")

next()
### ------------------------------------------------------------------------------------- ###
### A dictionary with a preset value for unknown key
# can be useful for graphs/trees
from collections import defaultdict

# construct a directed graph
graph = defaultdict(list)
a = [[1, 2], [1, 3], [2, 3], [3, 4], [2, 1]]

for v, i in a:
    graph[v] += [i]

print(graph)

### ------------------------------------------------------------------------------------- ###
### count the number of occurences of an element
from collections import Counter
s = "Gatsby and Daisy"
print(f"count of characters in \"{s}\": -> {Counter(s)}")

next()
### ------------------------------------------------------------------------------------- ###
### Sets
# unordered collection of unique elements
# useful in a lot of different contexts

a = [1, 2, 2, 3, 4]
print(f"{a} represented as a set: {set(a)}")

# USEFUL OPERATIONS
a = set(a)
b = set([1, 2, 5])

print(f"[-----] working with {a, b}")
print(f"* elements in 'a or b': {a.union(b)}")
print(f"* elements in 'a and b': {a.intersection(b)}")
print(f"* elements in 'a but not in b': {a.difference(b)}")
print(f"* test if 'every element in a is in b': {a.issubset(b)}")
print(f"* XOR {a^b} same as {a.symmetric_difference(b)} (in first or second, not in both)")



