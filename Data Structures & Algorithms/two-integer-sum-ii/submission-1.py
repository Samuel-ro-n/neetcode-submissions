class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n= len(numbers)
        result=[]
        for i in range(n):
            for j in range(i+1, n):
                Sum= numbers[i] + numbers[j]
                if Sum == target:
                    result+= [i+1, j+1]
        return result
        