class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        stack= []
        n, count, l= len(position), 0, 0
        while l<= (n-1):
            a, b= position.pop(), speed.pop()
            ans = (target - a)/b
            stack.append(ans)
            l+=1
        
        