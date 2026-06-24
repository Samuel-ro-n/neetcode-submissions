class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        NewSet=[[]]
        for num in nums:
            new_subsets = []
            for r in NewSet:
                values = r + [num]
                new_subsets.append(values)

            NewSet += new_subsets

        return NewSet
        

        