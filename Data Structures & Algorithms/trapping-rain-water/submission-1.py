class Solution:
    def trap(self, height: List[int]) -> int:
        max_val = 0
        # calculate left
        leftArray = []
        for i in range(0,len(height)):
            if(height[i] > max_val):
                leftArray.append(max_val)
                max_val = height[i]
            else:
                leftArray.append(max_val)
        # calculate right
        rightArray = []
        max_val = 0

        for i in reversed(range(0,len(height))):
            if(height[i] > max_val):
                rightArray.insert(0,max_val)
                max_val = height[i]
            else:
                rightArray.insert(0,max_val)

        # Min array
        print(leftArray)
        print(rightArray)
        minArray = []

        for i in range(len(leftArray)):
            minArray.append(min(leftArray[i], rightArray[i]))

        total = 0


        print(minArray)

        for i in range(len(height)):
            calc = minArray[i] - height[i]
            if(calc > 0):
                total += calc
            else:
                continue

        return total

        