class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i, cur):
            numsort= sorted(cur.copy())
            if numsort not in res:
                res.append(numsort)
            for j in range(i, len(nums)):
                cur.append(nums[j])
                dfs(j+1, cur)
                cur.pop()
        dfs(0,[])
        return res