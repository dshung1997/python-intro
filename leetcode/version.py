

def numsSameConsecDiff(N, K):
    numbers = []
    map_digits = [[] for i in range(10)]

    def generate_number(current_str, last_digit):
        if len(current_str) == N:

            numbers.append(int(current_str))
        else:
            next_digits = map_digits[last_digit]

            for d in next_digits:
                generate_number(current_str + str(d), d)

    if N == 1:
        return list(range(10))

    if K == 0:
        return [int(str(i) * N) for i in range(1, 10)]

    for d in range(0, 10):
        if d - K >= 0:
            map_digits[d].append(d - K)

        if d + K <= 9:
            map_digits[d].append(d + K)

    for d in range(1, 10):
        generate_number(str(d), d)

    return numbers


print(numsSameConsecDiff(3, 1))
