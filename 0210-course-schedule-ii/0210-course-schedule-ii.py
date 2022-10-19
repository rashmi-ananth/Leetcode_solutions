class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_lst = dict()
        indegree = dict()
        
        for i in range(numCourses):
            adj_lst[i] = []
            indegree[i] = 0
            
        for i, j in prerequisites:
            adj_lst[j].append(i)
            indegree[i] += 1
         
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
        visited = set()
        while len(queue) != 0:
            val = queue.pop(0)
            if val not in visited:
                order.append(val)
                visited.add(val)
            for i in adj_lst[val]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        
        if len(order) != numCourses:
            return []
        return order
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
