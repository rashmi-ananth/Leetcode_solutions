class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        visits = defaultdict(int)
        for i in range(len(cpdomains)):
            split = cpdomains[i].split(' ')
            count = int(split[0])
            domain = split[1]
            
            domain_split = domain.split('.')
            for i in range(len(domain_split)):
                combined = '.'.join(domain_split[i:])
                visits[combined] += count
                
        return_lst = []
        for key, value in visits.items():
            return_lst.append(str(value) + " " + key)
            
        return return_lst
            
            
        
        
        