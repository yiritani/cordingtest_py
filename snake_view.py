from typing import List


def snake_v1(chars):
    result = [[], [], []]
    insert_index = {0, 1, 2}
    index = 1

    for c, v in enumerate(chars):
        if c % 4 == 1:
            index = 0
        elif c % 2 == 0:
            index = 1
        elif c % 4 == 3:
            index = 2

        result[index].append(v)
        for i in insert_index - {index}:
            result[i].append(' ')

    return result


def snake_v2(char, depth):
    result = [[] for i in range(depth)]
    insert_index = {i for i in range(depth)}
    insert_depth = depth // 2

    pos = lambda insert_num: insert_num + 1
    neg = lambda insert_num: insert_num - 1
    ope = neg

    for i in char:
        result[insert_depth].append(i)
        for j in insert_index - {insert_depth}:
            result[j].append(' ')
        if insert_depth >= len(result) - 1:
            ope = neg
        if insert_depth <= 0:
            ope = pos
        insert_depth = ope(insert_depth)
    return result


if __name__ == '__main__':
    import string

    s = [j for i in range(3) for j in string.ascii_lowercase]
    c = ''.join(s)
    for i in snake_v2(c, 10):
        print(''.join(i))
