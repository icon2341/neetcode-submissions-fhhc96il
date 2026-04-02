class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # remember our intuition is that we go from left to right
        # we maintain a 2d stack of index spotted,height
        # if the heihgt we are evaling is LESS than the stack.peak, we know 
        # we are killing stack.peak and computing the area and giving it the index of peak
        # when we add it
        # otherwise just add it to the stack

        stack = []
        maxArea = 0
        heights_with_sentinel = heights
        heights_with_sentinel.append(0)

        for i in range(len(heights_with_sentinel)):
            height = heights_with_sentinel[i]
            # this guy is smaller
            print(stack, height)
            i_to_use = i
            while stack and height < stack[-1][1]:
                old_height = stack.pop()
                print("OLD HEIGHT", old_height)
                pot_area = old_height[1] * (i - old_height[0])
                if(pot_area > maxArea):
                    maxArea = pot_area
                    print("MAX AREA", maxArea)

                i_to_use = old_height[0]

            stack.append([i_to_use,height])
            
            
        return maxArea