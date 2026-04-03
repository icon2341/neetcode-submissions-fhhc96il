class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # given an array of integers
        # each number is between 0 and n+1
        # length of nums is n+1 i.e max + 1

        # every integer appears once except one integer which appears two or more times

        # trivial solution is to use a set or hashmap with quanitites
        # to find it.
        # second trivial solution is to use sorting but that modifes nums

        # we leverage the index of the array to do this somehow
        # I think we put each number in its corresponding index, starting with index 0
        # from there we keep bouncing around until we find that a identical number 
        # is already in one of the spaces we expected

        # [1,2,3,2,2]
        # []

        # here is the intelligent trick 
        # we loop through and we see if the index we are looking at has a negaive number
        # if it does, we know someone has been here before
        # and they would only have been here (since all numbs are >0) if 
        # there was a duplicate number that pointed to this index i.e same number again

        for num in nums:
            idx = abs(num) -1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1


        # the linked list approach is super interesting as well.
        # you use the VALUE at each index to determine where your cursor goes next.
        # using a fast and slow approach.








