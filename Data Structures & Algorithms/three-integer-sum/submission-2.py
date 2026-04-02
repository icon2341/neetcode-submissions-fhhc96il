class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        # we just do two sum for every k value in the set.
        output = []

        # [-4,-1,-1,-1,0,1,2]

        for i, k in enumerate(sortedNums):
            # check if k is a duplicate, if it is keep going because we already did it
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            # two sum
            leftIndex = i+1
            rightIndex = len(sortedNums)-1

            while leftIndex < rightIndex:
                testSum = sortedNums[leftIndex] + sortedNums[rightIndex] + k
                if(testSum < 0):
                    leftIndex += 1
                elif(testSum > 0):
                    rightIndex -=1
                else:
                    # PAIR FOUND!
                    output.append([sortedNums[leftIndex], sortedNums[rightIndex], k])

                    # skip any duplicates by nature (advance l till values are larger)

                    leftIndex += 1
                    while leftIndex < rightIndex and sortedNums[leftIndex] == sortedNums[leftIndex - 1]:
                        leftIndex += 1

        return output
