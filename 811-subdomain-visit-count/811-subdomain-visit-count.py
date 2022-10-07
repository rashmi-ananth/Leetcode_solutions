class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dictionary = dict()
        for i in range(len(cpdomains)):
            split = cpdomains[i].split(' ')
            integer = int(split[0])
            split_domain = split[1].split('.')
            for j in range(len(split_domain) ):
                join_domain = '.'.join(split_domain[j:])
                if join_domain in dictionary:
                    dictionary[join_domain] += integer
                else:
                    dictionary[join_domain] = integer
                    
                
        # print(dictionary)
        return_lst = []
        for key, value in dictionary.items():
            string = str(value) + " " + key
            return_lst.append(string)
            
            
        return return_lst
        
        
        