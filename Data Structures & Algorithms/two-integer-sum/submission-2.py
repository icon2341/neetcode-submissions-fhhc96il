class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}
        for i in range(0, len(nums)):
            numMap[nums[i]] = i

        print(numMap)
        
        for j in range(0, len(nums)):
            potential = target - nums[j]
            if potential in numMap.keys() and numMap[potential] != j:
                if (j < numMap[potential]):
                    return [j, numMap[potential]]
                else:
                    return [numMap[potential], j]
        