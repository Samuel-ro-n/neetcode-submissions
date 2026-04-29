class Solution:
    def findMin(self, nums: List[int]) -> int:
        n= len(nums)
        l, r= 0, n-1
        if not nums :
            return 0
        if n==1:
            return num[0]
        while l < r:
            if nums[l]< nums[r]:
                r-=1
            elif nums[l] > nums[r]:
                l+=1
            diff= abs(r - l)
            if diff==1:
                lowest= min(nums[l], nums[r])
        return lowest 