class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        j = 0
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            while count > k:
                if nums[j] == 0:
                    count -= 1
                j += 1
            res = max(res, i - j + 1)
        return res
        