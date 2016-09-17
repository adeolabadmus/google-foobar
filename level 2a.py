def answer(n, b):
    restrict_values(n, b)
    get_length.results = []  # set memoizer to store computed results
    return get_length(n, b)


def to_base(base, number):
    '''This function converts from base 10 to any other base'''
    base = int(base)
    number = int(number)
    rems = ''
    while True:
        rem = number % base
        rems = rems + str(rem)
        number = number/base
        if number == 0:
            break
    result = rems[::-1]  # reverse remainders
    return int(result)


def from_base(base, number):
    '''This function converts to base 10 from any base'''
    base = int(base)
    number = str(number)
    return int(number, base)


def subtract(tor, tee, base):
    '''This function subtracts two numbers, 'subtractor'
    and 'subractee' in the given base'''
    tor = int(tor)
    tee = int(tee)
    if base == 10:
        return tor - tee
    else:
        dec = from_base(base, tor) - from_base(base, tee)
        return to_base(base, dec)


def restrict_values(n, b):
    '''This function restricts values of 'k' and 'b',
    as stated in the question'''
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
    '''This function does the actual work'''
    y = ''.join(sorted(n))  # sort 'n' and assign to 'y'
    x = y[::-1]  # reverse 'y' to get decreasing order, 'x'

    diff = subtract(x, y, b)
    z_ = list(str(diff))  # convert diff between 'x' and 'y' to list

    # pad z as necessary
    offset = len(n) - len(z_)
    if offset:
        for i in range(offset):
            z_.insert(0, '0')
    z = ''.join(z_)

    if int(z) == 0:  # if answer is 0, return 1 as length
        return 1
    else:
        if z in get_length.results:  # if 'z' is already in results
            # if z is the last element, then length is 1
            if get_length.results[-1] == z:
                return 1
            else:
                # get distance between previous and present z
                z_index = get_length.results.index(z)
                return len(get_length.results) - z_index
        else:
            get_length.results.append(z)
    return get_length(z, b)
