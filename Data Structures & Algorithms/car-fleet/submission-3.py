class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse=True)
        stack = []
        for car in cars:
            time = (target-car[0])/car[1]

            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)
                