class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSideProducts = [1] * len(nums)
        rightSideProducts = [1] * len(nums)

        # [1,2,3,4]
        i = 0
        while(i < len(nums)):
            if(i == 1):
                leftSideProducts[i] = nums[i-1]
            elif(i >1):
                leftSideProducts[i] = nums[i-1]*leftSideProducts[i-1]
            i += 1

        i = len(nums)-1
        while(i >= 0):
            if(i == len(nums)-2):
                rightSideProducts[i] = nums[i+1]
            elif(i < len(nums)-2):
                rightSideProducts[i] = nums[i+1]*rightSideProducts[i+1]
            i -=1

        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = leftSideProducts[i] * rightSideProducts[i]

        print(leftSideProducts)
        print(rightSideProducts)
        return output

        