class Solution:
    def search(self, nums: List[int], target: int) -> int:
        long= len(nums)
        for i in range(long):
            if nums[i] == target:
                return i
        return -1