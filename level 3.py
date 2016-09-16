def answer(x, y):
    x, y = int(x), int(y)
    if (x < 1) or (x > 100000) or (y < 1) or (y > 100000):
        return
    prisoner_id = get_id_(x, y)
    return str(prisoner_id)


# Recursive Solution - Not optimal because of Python's recursion stack limits
def get_id(x, y):
    if y == 1:
        return sigma(x)
    return get_id(x, y - 1) + y + (x - 2)


# Iterative Solution
def get_id_(x, y, acc=0):
    while y > 1:
        x, y, acc = x, y-1, acc + y + x - 2
    return acc + sigma(x)


def sigma(n):
    return 1 if n == 1 else n * (n + 1) / 2
