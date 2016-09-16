import sys


def to_base(base, number):
    base = int(base)
    number = int(number)
    rems = ''
    while True:
        rem = number % base
        rems = rems + str(rem)
        number = number/base
        if number == 0:
            break
    result = rems[::-1]
    return int(result)


def from_base(base, number):
    base = int(base)
    number = str(number)
    return int(number, base)


def subtract(tor, tee, base):
    tor = int(tor)
    tee = int(tee)
    if base == 10:
        return tor - tee
    else:
        dec = from_base(base, tor) - from_base(base, tee)
        return to_base(base, dec)


def restrict_values(n, b):
    k = len(n)
    b = int(b)
    k_okay = (k >= 2) and (k <= 9)
    b_okay = (b >= 2) and (b <= 10)
    if not k_okay:
        raise Exception('length of n, k must satisfy 2 <= k <= 9')
    if not b_okay:
        raise Exception('base, b must satisfy 2 <= b <= 10')
    for i in n:
        if int(i) not in range(b):
            raise Exception('Invalid digits for base ', b)


def get_length(n, b):
    y = ''.join(sorted(n))
    x = y[::-1]

    diff = subtract(x, y, b)
    z_ = list(str(diff))

    offset = len(n) - len(z_)
    if offset:
        for i in range(offset):
            z_.insert(0, '0')
    z = ''.join(z_)
    if int(z) == 0:
        return 1
    else:
        if z in get_length.results:
            if get_length.results[-1] == z:
                return 1
            else:
                z_index = get_length.results.index(z)
                return len(get_length.results) - z_index
        else:
            get_length.results.append(z)
    return get_length(z, b)


def answer(n, b):
    restrict_values(n, b)
    get_length.results = []
    print get_length(n, b)

if __name__ == '__main__':
    answer(sys.argv[1], sys.argv[2])
