

def tryangle(height):
    result = [[1]*i for i in range(1, height)]

    for i in range(2, height-1):
        for j in range(1, len(result[i])-1):
            result[i][j] = result[i-1][j-1] + result[i-1][j]
    return result

def print_triangle(input_data):
    max_digit = len(str(max(input_data[-1])))
    width = max_digit + (max_digit %2) + 2
    for index, line in enumerate(input_data):
        numbers = ''.join([str(i).center(width, ' ') for i in line])
        print((' ' * int(width/2)) * (len(input_data) - index), numbers)


print_triangle(tryangle(5))
