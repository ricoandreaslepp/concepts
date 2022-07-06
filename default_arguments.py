def append(n, l=[]):
	l.append(n)
	return l

def append_with_constructor_reset(n, l=[]):
	l.__init__()
	l.append(n)
	return l

def correct_append(n, l=None):
	if l is None:
		l = []

	l.append(n)
	return n

# Default argument is only initialized once
print(append(1))
print(append(2))

# Checks the default argument value
print(correct_append(1))
print(correct_append(2))

# List object constructor is called before appending
print(append_with_constructor_reset(1))
print(append_with_constructor_reset(2))
