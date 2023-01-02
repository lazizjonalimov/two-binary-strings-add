def solution(a, b):
    length_bin = max(len(a), len(b))
    a = a.zfill(length_bin)
    b = b.zfill(length_bin)

    # result
    result = ''
    carry = 0

    for i in range(length_bin - 1, -1, -1):
        res = carry
        res += 1 if a[i] == '1' else 0
        res += 1 if b[i] == '1' else 0

        if res % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result

        if res < 2:
            carry = 0
        else:
            carry = 1

    if carry != 0:
        result = '1' + result

    return result.zfill(length_bin)


# Driver code
print(solution('1000', '111'))
