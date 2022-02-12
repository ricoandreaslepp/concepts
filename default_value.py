def append(n, l=[]):
	l.append(n)
	return l

def correct_append(n, l=None):
	if l is None:
		l = []

	l.append(n)
	return n

l1 = append(0)
print(l1)
l2 = append(1)
print(l2)

l3 = correct_append(0)
print(l3)
l4 = correct_append(2)
print(l4)