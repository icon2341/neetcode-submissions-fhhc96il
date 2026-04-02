class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}
        for num in nums:
            if(num) not in seen.keys():
                seen[num] = 1
            else:
                return True
        return False

        