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


def snake_v2(chars, depth):
    result = [[] for _ in range(depth)]
    insert_index = {i for i in range(depth)}
    index = depth // 2

    def pos(i):
        i += 1
        return i
    # pos = lambda i : i + 1
    neg = lambda i : i - 1
    ope = neg

    for i in chars:
        result[index].append(i)
        for j in insert_index - {index}:
            result[j].append(' ')
        if index <= 0:
            ope = pos
        elif index >= depth - 1:
            ope = neg


        index = ope(index)

    return result


if __name__ == '__main__':
    import string

    s = [i for j in range(3) for i in string.ascii_lowercase]
    c = ''.join(s)
    for i in snake_v2(c, 8):
        print(''.join(i))
