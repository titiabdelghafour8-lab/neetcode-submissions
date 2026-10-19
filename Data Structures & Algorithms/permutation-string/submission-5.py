class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        
        alphabet_map1 = { chr(i): 0 for i in range(ord('a'), ord('z') + 1) }
        alphabet_map2 = { chr(i): 0 for i in range(ord('a'), ord('z') + 1) }
        
        for i in range(n1):
            alphabet_map1[s1[i]] += 1
            alphabet_map2[s2[i]] += 1
        

        for k in range(n1, n2 + 1):
            if alphabet_map1 == alphabet_map2:
                return True
            else:
                if k == n2:
                    return False
                alphabet_map2[s2[k - n1]] -= 1
                alphabet_map2[s2[k]] += 1
        return False



            
                    