# 2 dau 1 1
def get(f, t):
    return max(0, (t - f - 2) >> 1)


def canPlaceFlowers(flowerbed, n):
    first = -1
    if 1 not in flowerbed:
        last = len(flowerbed)
        return get(first, last)

    first = flowerbed.index(1)
    prev = first
    count = 0
    for i in range(first + 1, len(flowerbed)):
        if flowerbed[i]:
            count += get(prev, i)
            prev = i

    return True if n <= count else False


print(canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 1))

# 1 1 -> 0
# 1 0 1 -> 0
# 1 0 0 1 -> 0
# 1 0 0 0 1 -> 1
# 1 2 3 4 5
# 3 -> 1
# 4 -> 1
# 5 -> 2
# 6 -> 2
# 7 -> 3
# max(0, ((to - from) >> 1) - 1)
