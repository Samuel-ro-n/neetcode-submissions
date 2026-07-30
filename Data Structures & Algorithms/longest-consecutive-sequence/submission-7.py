class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortout= sorted(set(nums))
        n= len(sortout)
        count=0
        reset=0
        for i in range(n-1):
            sub=sortout[i+1]-sortout[i]
            if sub==1:
                count+=1
            else:
                count = 0
            reset= max(reset, count)
        return reset+1           
       
               

        