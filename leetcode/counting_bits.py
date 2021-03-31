class Solution:
    def countBits(self, num):
        counts = [0, 1]

        if num <= 1:
            return counts[:num + 1]

        cur = 2

        while True:
            counts.append(1)
            i = 0
            for i in range(cur + 1, min(cur*2, num+1)):
                counts.append(counts[cur] + counts[i - cur])

            if i == 0 or i == num:
                break

            cur = cur * 2

        return counts


print(Solution().countBits(2))
