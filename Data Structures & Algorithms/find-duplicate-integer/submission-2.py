class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trivial solution use a set
        # to store seen values
        # the second we have a value that already exists 
        # in the set, then we return that value.

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
        #     else:
        #         seen.add(num)

        """
        The alternative,
        is given that the values are all less than len(nums)
        we loop through and use the val i as index
        we then find nums[index] and set that to negative
        if during the set operation we see the value is ALREADY negative
        then we know another value must have been there before etc
        """

        for val in nums:
            idx =abs(val) - 1

            if(nums[idx] < 0):
                return abs(val)
            else:
                nums[idx] *= -1


