from collections import Counter


def remover(X, Y):
	x_counter = Counter(X)
	y_counter = Counter(Y)
	for x, x_value in x_counter.items():
		y_value = y_counter.get(x)
		if not y_value:
			continue
		if x_value < y_value:
			X = [i for i in X if i != x]
		elif x_value > y_value:
			Y = [i for i in Y if i != x]
	print(X, Y)


remover([1, 2, 3, 4, 4, 5, 5, 8, 10], [4, 5, 5, 5, 6, 7, 8, 8, 10])
