class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        l, r=0, 1
        minnum=nums[l]
        while r<n:
            minnum= min(minnum, nums[r])
            r+=1
        return minnum
        
  
