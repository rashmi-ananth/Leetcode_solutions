class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        in_degree = dict()
        adj_lst = dict()
        
        for i in range(numCourses):
            in_degree[i] = 0
            adj_lst[i] = []
            
        for i in range(len(prerequisites)):
            adj_lst[prerequisites[i][1]].append(prerequisites[i][0])
            in_degree[prerequisites[i][0]] += 1
            
        queue = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)
              
        visited = set()
        return_lst = []
        while len(queue) > 0:
            val = queue.pop(0)
            visited.add(val)
            return_lst.append(val)
   
            for i in adj_lst[val]:
                in_degree[i] -= 1
                if in_degree[i] == 0 and i not in visited:
                    queue.append(i)
        
        if len(return_lst) != numCourses:
            return []
        return return_lst
            
            
            
        
       