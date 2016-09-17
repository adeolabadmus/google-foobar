def answer(s):
    # for each character in string s, call dec function dec if character
    #  is  lower case, else just use as-is
    ans = [dec(i) if i.islower() else i for i in s]
    return ''.join(ans)


def dec(s):
    # convert string to its ascii value, and deduct from 'a'
    o = ord(s) - 97
    # subtract from 'z' to determine new value
    n = 122 - o
    # return ascii character
    return chr(n)
