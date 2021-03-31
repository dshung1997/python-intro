class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        max_len = 1
        start = 0

        for i in range(1, len(s)):
            print("max_len", max_len)
            print("i", i)
            print("s[i-max_len-1:i+1]", s[i-max_len-1:i+1])
            print("s[i-max_len:i+1]", s[i-max_len:i+1])
            print()
            if i-max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len += 2
            elif i-max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i-max_len
                max_len += 1

        return s[start:start+max_len]


s = Solution()
print(s.longestPalindrome("babad"))
