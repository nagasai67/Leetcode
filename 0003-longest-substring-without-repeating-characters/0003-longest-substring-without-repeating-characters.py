class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        d = set()
        res = 0
        for i in range(len(s)):
            while s[i] in d:
                d.remove(s[j])
                j += 1

            d.add(s[i])
            res = max(res,i-j+1)
        return res
        



        