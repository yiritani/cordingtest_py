import time


def continued_max_num(l):
	result = 0
	for index in range(len(l)):
		for i in range(index, len(l)):
			sumed_continue = sum(l[index:i+1])
			if result < sumed_continue:
				result = sumed_continue
	print(result)



def tmp_continued_max_num(l):
	result , sum_sequence = 0, 0
	for num in l:
		tmp_sequence = sum_sequence + num
		if num < tmp_sequence:
			sum_sequence = tmp_sequence
		else:
			sum_sequence = num

		if result < sum_sequence:
			result = sum_sequence
	print(result)




def circular(l):
	min_result, minus_sequence = 0, 0
	for num in l:
		tmp = minus_sequence - num
		if num > tmp:
			minus_sequence = num
		else:
			minus_sequence = num

		if min_result > minus_sequence:
			min_result = minus_sequence
	print(min_result)






l = [1 ,-2 ,3 ,6 ,-1 ,2 ,4 ,-5 ,2]
circular(l)
