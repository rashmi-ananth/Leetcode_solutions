class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        
        nums1_set = list(set(nums1))
        nums2_set = set(nums2)
        
        return_arr = []
        
        for i in range(len(nums1_set)):
            
            if nums1_set[i] in nums2_set:
                return_arr.append(nums1_set[i])
        
        return return_arr
        
        