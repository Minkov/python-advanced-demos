def print_line(n):
    line = [str(i) for i in range(1, n + 1)]
    print(' '.join(line))


def print_triangle(n):
    for i in range(n):
        print_line(i + 1)

    for i in range(n - 1):
        print_line(n - i - 1)

    # for i in range(n - 1, -1, -1):
    #     print_line(i)
