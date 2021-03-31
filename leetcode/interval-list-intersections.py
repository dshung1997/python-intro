class Solution:
    def intervalIntersection(self, A1, A2):
        if len(A1) == 0 or len(A2) == 0:
            return []

        i1, i2 = 0, 0
        res = []
        while i1 < len(A1) and i2 < len(A2):
            s1, e1 = A1[i1]
            s2, e2 = A2[i2]

            if s1 <= e2 and s2 <= e1:
                res.append([max(s1, s2), min(e1, e2)])

            if e1 <= e2:
                i1 += 1
            else:
                i2 += 1

        return res
