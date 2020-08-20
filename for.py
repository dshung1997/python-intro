def checkPossibility(nums):
    l = len(nums)

    if l == 2:
        return True

    if l == 3:
        if nums[0] > nums[1] > nums[2]:
            return False
        else:
            return True

    # l >= 4
    count = 0
    for i in range(len(nums) - 1):
        n = nums[i]
        next_n = nums[i+1]

        if next_n < n:
            count += 1

            if count >= 2:
                return False
            else:
                if i == 0 or i == l - 2:
                    continue
                else:
                    if nums[i] > nums[i+2] and nums[i-1] > nums[i+1]:
                        return False

    return True


print(checkPossibility([3, 4, 2, 3]))

# 4 2 1
# a1 >= a2 >= a3
# a1 a2 a3 a4

# when a2 > a3
# if a1 > a3 and a2 > a4, no hope

#  2 3 2 3
