class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortout= sorted(nums)
        n= len(sortout)
        count=0
        for i in range(n-1):
            sub=sortout[i+1]-sortout[i]
            if sub==1:
                count+=1
        return count+1           
       
               

        