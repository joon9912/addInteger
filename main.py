# add integer


def ladd(u, v):
    n = len(u) if (len(u) > len(v)) else len(v)
    result = []
    carry = 0
    for k in range(n):
        i = u[k] if (k < len(u)) else 0
        j = v[k] if (k < len(v)) else 0
        value = i + j + carry
        carry = value // 10
        result.append(value % 10)
    if (carry > 0):
        result.append(carry)
    return result


if __name__ == '__main__':
    u = [3, 2, 1]   # u = 123
    v = [5, 4]      # v = 45
    print(123 + 45)
    print(ladd(u, v)[::-1])

    u = [2, 3, 8, 7, 6, 5]      # u = 567832
    v = [3, 2, 7, 3, 2, 4, 9]   # v = 9423723
    print(567832 + 9423723)
    print(ladd(u, v)[::-1])

