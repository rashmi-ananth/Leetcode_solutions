class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_lst = [0]
        
        for i in range(len(nums)):
            self.sum_lst.append(nums[i] + self.sum_lst[i])
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.sum_lst[right + 1] - self.sum_lst[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# [0,-2,-2,1,-4,-2,-3]