class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trivial solution use a set
        # to store seen values
        # the second we have a value that already exists 
        # in the set, then we return that value.

        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)
