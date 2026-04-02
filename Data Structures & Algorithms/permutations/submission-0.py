class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        is_used = [0] * len(nums)

        def dfs(i,path,is_used):
            if i == len(nums):
                res.append(path[:])
                return
            for idx in range(0, len(nums)):
                if not is_used[idx]:
                    path.append(nums[idx])
                    is_used[idx]=1
                    dfs(i+1, path, is_used)
                    is_used[idx] =0
                    path.pop()
        dfs(0,[],is_used)
        return res