a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (3, 4, 1, 2, 7, 6, 5, 8)
c = {5, 6, 7, 8, 1, 2, 3, 4}


def check(l, t, d):
    if len(l) != len(t) or len(t) != len(d) or len(d) != len(l):
        return False

    for a in l:
        if a not in t or a not in d:
            return False

    return True


print(check(a, b, c))
