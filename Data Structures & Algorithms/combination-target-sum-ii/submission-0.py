class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. Sort the candidates. 
        # This is CRUCIAL because it brings duplicate numbers together (e.g., [1, 1, 2]).
        # It also allows us to stop early if the total exceeds the target.
        candidates.sort()

        def dfs(i, cur, total):
            # Success Case: We reached exactly the target sum
            if total == target:
                res.append(cur.copy())
                return
            
            # Failure Case: We went over the target or ran out of numbers
            if total > target or i == len(candidates):
                return

            # --- DECISION 1: INCLUDE candidates[i] ---
            # We add the current number to our path and move to the next index
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            
            # Backtrack: Remove the number so we can explore "Decision 2" with a clean path
            cur.pop()

            # --- DECISION 2: SKIP candidates[i] ---
            # To avoid duplicate combinations, if we decide NOT to use a '1', 
            # we must skip ALL '1's at this current level of the recursion.
            # Otherwise, the algorithm would pick the *next* '1' and result in the same set.
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            # Move to the next index that is a completely different number
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


        # so the decisions are 

        # we either use a num[i], and from there we can determine to use ANOTHER num[i] or again continue 
        # if dont use the num[i] then we must skip till the end of the num[i] so that we can test out with a fresh value 
        # otherwise we would be making duplicates since we assume that the first branch 
        # prob tested some permutatin of num[i] already
        # so the simple decision is to use num[i]'s or do not use any of num[i's] cuz using the nth num[i] even if we skip num[1] will result in 
        # a duplicate combination