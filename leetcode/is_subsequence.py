import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        def get_char_index(c):
            return ord(c) - 97

        index_list = [[] for i in range(0, 26)]

        for i, c in enumerate(t):
            index_list[get_char_index(c)].append(i)

        m = -1
        for c in s:
            i = bisect.bisect_left(index_list[get_char_index(c)], m)

            if i >= len(index_list[get_char_index(c)]):
                return False

            m = index_list[get_char_index(c)][i] + 1

        return True


print(Solution().isSubsequence("aaaaaa", "bbaaaa"))
