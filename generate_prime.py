def gen_prime_1(n):
	result = []

	for first_hie in range(2, n):
		for second_hie in range(2, first_hie):
			if first_hie % second_hie == 0:
				break
		else:
			result.append(first_hie)

	return result


def gen_prime_2(n):
	result = []
	cache = {}

	for first_hie in range(2, n):
		if cache.get(first_hie):
			continue
		result.append(first_hie)
		for cache_num in range(first_hie, n, first_hie):
			cache[cache_num] = True

	return result


import time

# start = time.time()
# print(gen_prime_1(20000))
# print(time.time() - start)
start = time.time()
print(gen_prime_2(1000000))
print(time.time() - start)
