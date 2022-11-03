class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Time: O(M + N)
        # Space: Time: O(M)
        
        nums1_copy = []
        for i in range(m):
            nums1_copy.append(nums1[i])
        idx1 = 0
        idx2 = 0
        
        
        
        for i in range(m+n):
            # print(nums1, nums1_copy[idx1], nums2[idx2])
            if idx1 < m and idx2 < n:
                if nums1_copy[idx1] <= nums2[idx2]:
                    nums1[i] = nums1_copy[idx1]
                    idx1 += 1
                else:
                    nums1[i] = nums2[idx2]
                    idx2 += 1
            else:
                break
        
        if idx1 < m:
            while idx1 < m:
                nums1[i] = nums1_copy[idx1]
                idx1 += 1
                i += 1
               

        if idx2 < n:
            while idx2 < n:
                nums1[i] = nums2[idx2]
                idx2 += 1
                i += 1


            
        