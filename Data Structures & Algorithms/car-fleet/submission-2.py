class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Combine and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        for pos, spd in cars:
            # 2. Calculate time to reach target
            time = (target - pos) / spd
            
            # 3. If the stack is empty, or this car takes MORE time than
            # the fleet in front, it becomes the lead of a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
            
            # If time <= stack[-1], the car joins the fleet ahead. 
            # We don't add it to the stack because it's limited by the slower car.

        return len(stack)