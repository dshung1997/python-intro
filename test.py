l = [3, 4, 1, 2, 6, 7, 8, 10]


def calc_max(x, y):
    return x ^ ((x ^ y) & -(x < y))


max1 = l[0]
max2 = l[0]
n = len(l)
for i in range(1, n):
    max1 = calc_max(max1, l[i])
    max2 = calc_max(max1, l[i])

print("Second highest number is : ", str(max2))
