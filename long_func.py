from functools import lru_cache


def memoize(f):
	cache = {}

	def _wrapper(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]

	return _wrapper


@memoize
def long_func(n):
	r = 0
	for i in range(10000000):
		r += n * i
	return r


for i in range(5):
	print(long_func(i))
for i in range(5):
	print(long_func(i+1))
