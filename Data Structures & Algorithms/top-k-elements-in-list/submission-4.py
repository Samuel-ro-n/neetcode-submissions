class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        numdict={}
        for i in nums:
            numdict[i]= 1 + numdict.get(i, 0)
        SBF= sorted(numdict.items(), key=lambda x:x[1], reverse=True)
        for x, y in SBF[:k]:
            ans.append(x)
        return ans
        