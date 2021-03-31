class Solution:
    def partitionLabels(self, s):
        rightmost = {c: i for i, c in enumerate(s)}
        print(rightmost)
        counts = [0] * 26

        def get_index(c):
            return ord(c) - ord('a')

        for c in s:
            counts[get_index(c)] += 1

        char_left_to_partition = 0
        counter = 0
        res = []
        for c in s:
            if char_left_to_partition == 0:
                res.append(counter)
                counter = 0

            char_left_to_partition += counts[get_index(c)]
            counts[get_index(c)] = 0
            counter += 1
            char_left_to_partition -= 1

        res.append(counter)
        return res[1:]


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
# print(Solution().partitionLabels("a"))
