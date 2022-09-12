class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
 
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_arr = []
        for i in range(len(self.nums)):
            dot_arr.append(self.nums[i] * vec.nums[i])
        return sum(dot_arr)
            
        
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)