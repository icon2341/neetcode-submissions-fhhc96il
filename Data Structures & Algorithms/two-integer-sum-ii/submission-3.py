class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer = 0
        rightPointer = len(numbers)-1

        while(leftPointer < rightPointer):
            numSum = numbers[leftPointer] + numbers[rightPointer]
            if numSum < target:
                leftPointer += 1
            elif numSum > target:
                rightPointer -= 1 
            else:
                return [leftPointer+1, rightPointer+1]