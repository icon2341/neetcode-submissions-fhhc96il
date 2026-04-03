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
        # using a fast slow approach 2 times not just one.

        # First, we do a fast and slow algorithm, 
        # and we use the value at idx to determine what index we head to.

        # If there is a duplicate, both pointers will settle to an identical value at some point.
        # this is because lets say 2 is the duplicate
        #  2 idx 3 and 2 idx 7
        # fast will get to (2,3) then head to (x,2)
        # nomatter what x is fast will traverse like normal n times 
        # until it gets to the SECOND 2, which will send it back to (x,2)
        # this will create a cycle.

        # eventually the two will meet since slow will do the same thing.

        # This tells us that there IS a cycle and we roughly know where it is since the two met
        # to determine what value it is in specific 
        # we have a new pointer slow2 walk slowly
        # we have slow1 walk slowly as well
        # once slow2 and slow meet again which they will since slow1 is in a cycle
        # and eventually they will meet tat th








