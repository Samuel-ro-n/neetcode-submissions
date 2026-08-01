class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n= len(temperatures)
        l, r= 0, 1
        if n == 0:
            return result
        while l < (n-1):
            if r == n:
                stack.append(0)
                l+=1
                r=l + 1
            elif temperatures[l]< temperatures[r]:
                stack.append(r-l)
                l+=1
                r=l +1   
            else:
                r+=1
            
        stack.append(0)
        return stack
            



        




        