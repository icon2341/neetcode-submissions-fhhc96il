class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # we found an increasing temprature!
                stackT, stackInd = stack.pop()
                # get the first decreasing temp and its index and compare it
                output[stackInd] = i - stackInd
                # keep popping them off until the values are populated
            stack.append((t,i))

        return output