
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        L: List[List[str]] = []        
        anagram_map: dict[str, List[str]] = {}
        for s in strs:
            test = "".join(sorted(s))
            if test in anagram_map:
                anagram_map[test].append(s)
            else:
                anagram_map[test] = [s]
        return list(anagram_map.values())

                
