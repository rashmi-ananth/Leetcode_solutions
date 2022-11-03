class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - n
        for i in range(len(nums2)):
            nums1[idx] = nums2[i]
            idx += 1

        nums1.sort()
            
        