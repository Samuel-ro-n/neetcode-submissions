class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined= [[x, y] for x, y in zip(position, speed)]
        stack=[]
        for x, y in sorted(combined)[::-1]:
            stack.append((target - x)/y)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        
        