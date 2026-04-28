class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ls=len(s)
        Lt=len(t)
        if Ls != Lt:
            return False
        return sorted(s)== sorted(t)

        