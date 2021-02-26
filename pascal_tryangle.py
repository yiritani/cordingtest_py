

def tryangle(depth: int):
    tryangle_list = [[1] * (i + 1) for i in range(depth)]

    for i in range(2, len(tryangle_list)):
        for j in range(1, len(tryangle_list[i])-1):
            tryangle_list[i][j] = tryangle_list[i-1][j-1] + tryangle_list[i-1][j]

    return tryangle_list


def print_tryangle(numbers):
    width = 6
    for i, k in enumerate(numbers):
        line = ''.join([str(i).center(6, ' ') for i in k])

        print((' ' * int(width/2)) * (len(numbers) - i), line)



print_tryangle(tryangle(5))