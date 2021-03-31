import math


class UF:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for _ in range(N)]
        self.max_size = 1

    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.max_size = max(self.max_size, self.size[root_y])


class Solution:

    def put_or_union(self, d, uf, k, val):
        if k not in d:
            d[k] = val
        else:
            uf.union(val, d[k])

    def largestComponentSize(self, A):
        N = len(A)

        d = dict()

        uf = UF(N)

        for i in range(N):
            a = A[i]
            s = math.floor(math.sqrt(a)) + 2

            for j in range(2, s):
                if a % j == 0:
                    self.put_or_union(d, uf, j, i)

                    if a != j:
                        self.put_or_union(d, uf, a // j, i)

            if a != 1:
                self.put_or_union(d, uf, a, i)

        return uf.max_size


print(Solution().largestComponentSize([1, 2, 3, 4, 5, 6, 7, 8, 9]))
