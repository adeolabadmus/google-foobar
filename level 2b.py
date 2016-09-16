import sys


def answer(x, y):
    x, y = int(x), int(y)
    if (x < 1) or (x > 100000) or (y < 1) or (y > 100000):
        return
    prisoner_id = get_id(x, y)
    return str(prisoner_id)


def get_id(x, y):
    if y == 1:
        return sigma(x)
    return get_id(x, y - 1) + y + (x - 2)


def sigma(n):
    return 1 if n == 1 else n * (n + 1) / 2

print answer(sys.argv[1], sys.argv[2])
