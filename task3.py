numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]


def filter_func(item):
    if item > 50 and item % 2 != 0:
        return True
    else:
        return False


print(list(filter(filter_func, numbers)))
