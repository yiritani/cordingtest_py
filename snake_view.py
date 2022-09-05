import string


def snake_v1(l):
	parent_snake = [[], [], []]
	escape_sequence = {0, 1, 2}
	now_cnt = 1
	neg = lambda x: x - 1
	pos = lambda x: x + 1
	cal_func = neg

	for i in l:
		parent_snake[now_cnt].append(i)
		for escape in escape_sequence - {now_cnt}:
			parent_snake[escape].append(' ')
		if 2 <= now_cnt:
			cal_func = neg
		elif now_cnt <= 0:
			cal_func = pos
		now_cnt = cal_func(now_cnt)

	return parent_snake


def snake_v2(l, height):
	parent_snake = [[] for _ in range(height)]
	escape_sequence = {i for i in range(height)}
	now_cnt = height // 2
	neg = lambda x: x - 1
	pos = lambda x: x + 1
	cal_func = neg

	for i in l:
		parent_snake[now_cnt].append(i)
		for escape in escape_sequence - {now_cnt}:
			parent_snake[escape].append(' ')
		if height-1 <= now_cnt:
			cal_func = neg
		elif now_cnt <= 0:
			cal_func = pos
		now_cnt = cal_func(now_cnt)

	return parent_snake


l = []
for i in range(10):
	l.append(str(i))

i = list(string.ascii_lowercase) * 5
for s in snake_v2(i, 10):
	# print(s)
	print(''.join(s))
