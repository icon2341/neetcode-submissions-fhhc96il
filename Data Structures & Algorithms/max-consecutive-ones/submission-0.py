class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s1 = 0

        maxNums = 0
        counter = 0
        while(s1 < len(nums)):
            if(nums[s1] == 1):
                counter += 1
                if(counter >= maxNums):
                    maxNums = counter
            else:
                counter = 0
            
            s1 += 1
        return maxNums
