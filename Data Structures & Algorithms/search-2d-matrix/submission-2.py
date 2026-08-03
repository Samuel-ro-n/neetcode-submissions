class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new=[]
        for c in matrix:
            new +=c
        if target not in new:
            return False
        else:
            return  True