class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            if value in seen.keys():
                return [seen[value], i]
            else:
                seen[nums[i]] = i
        return