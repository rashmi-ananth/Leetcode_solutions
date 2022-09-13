class Solution:
    def frequencySort(self, s: str) -> str:
        
        
        dictionary = defaultdict(int)

        for i in s:
            dictionary[i] += 1
            
        sorted_items = sorted(dictionary.items(), key=lambda x: -x[1])
        
        arr = []

        
        for k, v in sorted_items:
            arr.append(k * v)
            
         
        
        return ''.join(arr)