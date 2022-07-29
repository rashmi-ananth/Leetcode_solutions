class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
 
        
        visited = set()
        counter = 0
        dictionary = dict()
        nums.sort()
        
        
        for i in range(len(nums)):
            val = nums[i] - k
            if val in visited and nums[i] not in dictionary.keys():
                counter += 1
                dictionary[nums[i]] = val
               # print(nums[i], val)
            visited.add(nums[i])
        return counter
                
            
            
        
        
        
 