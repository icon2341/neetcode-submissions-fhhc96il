class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = -1

        # n^2 solution is pretty trivial just calculate all combinations of the bars.
        # a smarter solution might be 
        leftIndex = 0
        rightIndex = len(heights)-1

        # Pro tips to remember about two pointer
        

        while leftIndex < rightIndex:
            # calculate area
            evalArea = min(heights[leftIndex], heights[rightIndex]) * (rightIndex - leftIndex) 

            print(evalArea,leftIndex, rightIndex,heights[leftIndex], heights[rightIndex])
            if(evalArea > maxarea):
                maxarea = evalArea
            if heights[leftIndex] <= heights[rightIndex] :
                leftIndex += 1
            else:
                rightIndex -= 1

        return maxarea