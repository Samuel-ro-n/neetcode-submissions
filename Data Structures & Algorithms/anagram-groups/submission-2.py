class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordict= {}
        for word in strs:
            sw= ''.join.sorted(word)
            if sw not in wordict:
                wordict[sw]== []
            wordict[sw].append(word)
        return wordict.values
