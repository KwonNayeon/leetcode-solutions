class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
        
        return list(anagram_dict.values())
        