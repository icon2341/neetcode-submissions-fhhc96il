class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # Sorting helps with efficiency, allowing us to break early
        nums.sort() 

        def backtracking(start, path, current_sum):
            if current_sum == target:
                res.append(list(path))
                return
            
            for i in range(start, len(nums)):
                # Optimization: if adding this number exceeds target, 
                # no need to check numbers after it (since nums is sorted)
                if current_sum + nums[i] > target:
                    break
                
                path.append(nums[i])
                # We pass 'i' as the new 'start' because we can reuse the same number
                backtracking(i, path, current_sum + nums[i])
                path.pop()

        backtracking(0, [], 0)
        return res