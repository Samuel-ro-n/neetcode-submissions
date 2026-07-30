class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n= len(nums)
        for i in range(n):
            for j in range(i+1, n-1):
                Sum= nums[i]+nums[j]+nums[j+1]
                if Sum==0:
                    result.append([nums[i], nums[j], nums[j+1]])
        result = [list(triplet) for triplet in set(tuple(sorted(triplet)) for triplet in result)]
        return result