

def snake(str, depth):
    start = depth // 2
    insert_list = [[] for i in range(depth)]
    insert_index = {i for i in range(depth)}

    pos = lambda i : i + 1
    neg = lambda i : i - 1
    ope = neg

    for i in str:
        insert_list[start].append(i)
        for rest in insert_index - {start}:
            insert_list[rest].append(' ')

        if start <= 0:
            ope = pos
        elif start >= depth-1:
            ope = neg

        start = ope(start)

    return insert_list



import string
sss = [j for i in range(5) for j in string.ascii_uppercase]
for i in snake(sss, 8):
    print(''.join(i))