from typing import List


def snake_v1(chars):
    result = [[],[],[]]
    result_index = {0,1,2}
    insert_index = 1

    for i, v in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2

        result[insert_index].append(v)

        for rest in result_index - {insert_index}:
            result[rest].append(' ')

    return result

def snake_v2(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_index = {i for i in range(depth)}
    insert_index = depth // 2

    pos = lambda i: i + 1
    neg = lambda i: i - 1

    ope = neg

    for i in chars:
        result[insert_index].append(i)
        for rest in result_index - {insert_index}:
            result[rest].append(' ')
        if insert_index <= 0:
            ope = pos
        if insert_index >= depth - 1:
            ope = neg

        insert_index = ope(insert_index)


    return result





if __name__ == '__main__':
    import string
    char_list = [s for _ in range(2) for s in string.ascii_lowercase]
    c = ''.join(char_list)
    for cc in snake_v2(c, 10):
        print(''.join(cc))
