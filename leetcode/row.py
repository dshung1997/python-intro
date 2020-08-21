def getRow(n):
    result = []
    a = 1

    result.append(a)

    for r in range(0, n // 2):
        a = (n - r) * result[r] // (r+1)
        result.append(a)
        r += 1

    if n % 2 == 0:
        result = result[:-1] + [result[-1]] + result[:-1][::-1]
    else:
        result = result + result[::-1]

    return result


print(getRow(0))
print(getRow(1))
print(getRow(2))
print(getRow(3))
print(getRow(4))
print(getRow(5))
