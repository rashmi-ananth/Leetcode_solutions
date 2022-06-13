class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return_lst = [0] * len(nums)
        # return_lst[0] = nums[0]

        
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])

        return max(nums)