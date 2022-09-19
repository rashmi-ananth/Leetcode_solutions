class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        
        
        
        
        
        0,1,2,3,4,5,6,7
        7,0,1,2,3,4,5,6
        4,5,6,7,0,1,2,3
        3,4,5,6,7,8,0,1,2
        
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if target==nums[mid]:
                return mid
 
            if nums[l]<= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
        


  
        
        
        
        
        
        
        
        
        
        

# [4,5,6,7,0,1,2]

#         def binarySearch(nums, l, r):
#             print('hi')
#             if l > r:
#                 return -1
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             print(nums[mid])
            
            
#             if nums[mid] > target and nums[l] <= target:
#                 return binarySearch(nums, l, mid)
#             if nums[mid] > target and nums[r-1] <= nums[mid]:
#                 return binarySearch(nums, mid + 1, r)
#             if nums[mid] < target and nums[r-1] <= target:
#                 return binarySearch(nums, mid + 1, r)
#             if nums[mid] < target and nums[l] >= target:
#                 return binarySearch(nums, l, mid)
                
 
            
        return binarySearch(nums, 0, len(nums))