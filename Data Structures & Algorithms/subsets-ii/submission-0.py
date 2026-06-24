class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        Newset=[[]]
        for num in nums:
            subset=[]
            for i in Newset:
                Value= i + [num]
                subset.append(Value)
            Newset += subset
        unique=[]
        for subset in Newset:
            subset.sort()
            if subset not in unique:
                unique.append(subset)
        return unique