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
import itertools

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
from collections import defaultdict
d = defaultdict()

### ------------------------------------------------------------------------------------- ###
### count the number of occurences of an element
from collections import Counter
s = "Gatsby and Daisy"
print(f"count of characters in \"{s}\": -> {Counter(s)}")

