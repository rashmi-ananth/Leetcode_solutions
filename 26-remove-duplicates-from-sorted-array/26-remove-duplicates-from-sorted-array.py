class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                
          
        return j + 1
                
            
        
        # duplicates = 0
        
#         idx = 1
#         currIdx = 0
        

#         # 0,1,1,_,_,_,2,_,3,_,4
        
        
#         while idx < len(nums):
#             if nums[idx] == nums[currIdx]:
#                 duplicates += 1
#                 nums[idx] = "_"
#                 idx += 1
 
#             else:
#                 currIdx = idx
#                 idx += 1

#         curr_idx2 = 0
#         non_dash = 0
        
#         print(nums)
    
#         while non_dash < len(nums):
#             if nums[non_dash] != "_":
#                 temp = nums[curr_idx2]
#                 nums[curr_idx2] = nums[non_dash]
#                 nums[non_dash] = temp
                
#                 curr_idx2 += 1
#                 non_dash += 1
#             else:
#                 non_dash += 1
                
        
        
        
        return duplicates 
                
                
                
            
        
                
                
            
            
        

        
        