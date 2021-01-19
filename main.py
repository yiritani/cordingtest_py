from typing import List

def snake_string_v1(nums: str)-> List[List[str]]:
    result = [[],[],[]]
    result_index = {0,1,2}
    insert_index = 1
    for i, s in enumerate(nums):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2

        result[result_index].append(s)
        for rest_index in rest_index - {insert_index}:
            result[rest_index].append(' ')

    return result










if __name__ == '__main__':

    numbers = [str(i) for j in range(5) for i in range(10)]
    strings = ''.join(numbers)
    for line in snake_string_v1(strings):
        print(''.join(line))

