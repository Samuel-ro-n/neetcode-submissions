class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nset=[]
        countS={}
        for i in range(len(nums)):
            countS[nums[i]]= 1 + countS.get(nums[i], 0)
        sorted_by_freq = sorted(countS.items())
        for t, v in sorted_by_freq:
            if v >= k:
                nset.append(t)
        return nset
        