import bisect


class Solution:
    def findRightInterval(self, intervals):
        l = sorted((e[0], i) for i, e in enumerate(intervals))
        res = []

        for e in intervals:
            r = bisect.bisect_left(l, (e[1], ))
            res.append(l[r][1] if r < len(l) else -1)

        return res


s = Solution()
print(s.findRightInterval([[3, 4], [2, 3], [1, 2]]))
