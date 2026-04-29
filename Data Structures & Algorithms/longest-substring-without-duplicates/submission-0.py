class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        sub=[]
        for i in range(len(s)):
            if s[i] not in sub:
                sub.append(s[i])
                count+=1
        return count
        