def get_unique_number(path):
    if not path:
        return None

    # Count the first number in the list
    # If count = 1, it's the answer
    # Otherwise, count is K
    first_number = -1
    count_first_number = 0

    # The other numbers appear exactly K times, so count number of 1s and 0s at each position
    # If the total number of a bit is divisible by K, the bit is turned on, otherwise, it's turned off
    count = [0 for _ in range(0, 32)]

    with open(path) as fp:
        Lines = fp.readlines()
        for line in Lines:
            n = int(line)

            # Set the first number
            if first_number == -1:
                first_number = n

            # Increase the counter
            if first_number == n:
                count_first_number += 1
            
            # Count bits
            for i in range(0, 32):
                count[i] += (n & 1)
                n >>= 1

        if count_first_number == 1:
            return first_number

        for i in range(0, 32):
            count[i] %= count_first_number

        # Bit 0th is the rightmost
        count.reverse()
        
        # Join the bits
        return int("".join([str(x) for x in count]), 2)
            
# print(get_unique_number("big_data.txt"))