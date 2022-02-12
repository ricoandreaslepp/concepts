import logging
import time

start = time.perf_counter()

def testing():
	# check types with isinstance
	x = 2
	if isinstance(x, int):
		logging.debug(f"x is {x}") # use string formatting

	a = [1,2,3]
	b = [4,5,6]
	if a and b: # don't need anything else

		for i, (ai, bi) in enumerate(zip(a, b)):
			logging.info(f"{i} {(ai, bi)}")

def main():
	level = logging.DEBUG # easy to setup and better than just random printing
	fmt = '[%(levelname)s] %(asctime)s - %(message)s'
	logging.basicConfig(level=level, format=fmt)

	testing()

if __name__ == "__main__": # useful if you need to reuse stuff from different files
	main()
	print(time.perf_counter() - start) # use perf_counter for timing your code
