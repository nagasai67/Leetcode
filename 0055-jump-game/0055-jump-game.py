class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_pos = len(nums) - 1
        for i in range(len(nums) - 2,-1,-1):
            if i + nums[i] >= final_pos:
                final_pos = i 
        return final_pos == 0
        