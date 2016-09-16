def answer(s):
    ans = [dec(i) if i.islower() else i for i in s]
    return ''.join(ans)


def dec(s):
    o = ord(s) - 97
    n = 122 - o
    return chr(n)

print answer('vmxibkgrlm')
