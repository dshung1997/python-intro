class BIT:
    def __init__(self, n):
        self.n = n
        self.bits = [0] * (n + 1)
        self.total = 0
        # Total stores the total sum of the tree. This makes retrieving right sums more efficient.

    def update(self, index, value):
        index += 1
        self.total += value
        while index <= self.n:
            self.bits[index] += value
            index += index & (-index)

    def getsum(self, index: int):
        if index < 0:
            # `~index == - index - 1`.
            # `bit.getsum(~index)` will retrieve the sum of values from `index + 1` to `n`.
            return self.total - self.getsum(~index)
        if index >= self.n:
            return self.total
        ans = 0
        index += 1
        while index > 0:
            ans += self.bits[index]
            index -= index & (-index)
        return ans

    def __repr__(self):
        return f"n={self.n} total={self.total} bits={self.bits}"


class Solution:

    def numTeams(self, rating):
        n = len(rating)
        mapping = {r: i for i, r in enumerate(sorted(rating))}
        print("sorted", sorted(rating))
        print("mapping", mapping)
        left_counts = BIT(n)
        right_counts = BIT(n)
        for r in rating[1:]:
            print(f"r: {r} | {mapping[r]}")
            right_counts.update(mapping[r], 1)
            print(right_counts)
        ans = 0
        left_counts.update(mapping[rating[0]], 1)
        for r in rating[1: -1]:
            index = mapping[r]
            right_counts.update(index, -1)
            ans += left_counts.getsum(index) * right_counts.getsum(~index)
            ans += left_counts.getsum(~index) * right_counts.getsum(index)
            left_counts.update(index, 1)
        return ans


rating = [2, 5, 3, 4, 1]
s = Solution()
print(rating)
print(s.numTeams(rating))
