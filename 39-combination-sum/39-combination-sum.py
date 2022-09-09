class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        return_lst = []
        def dfs(total, lst, start):
            if total == target:
                return_lst.append(lst)
                return
            
            if total > target:
                return
            

            for i in range(start, len(candidates)):
                dfs(total + candidates[i], lst + [candidates[i]], i)

                     
        total = 0
        dfs(total, [], 0)
        
        return return_lst
        
        
