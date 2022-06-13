class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return_lst = [0] * len(nums)
        return_lst[0] = nums[0]

        for i in range(1, len(nums)):
            return_lst[i] = max(nums[i], nums[i] + return_lst[i-1])

        return max(return_lst)