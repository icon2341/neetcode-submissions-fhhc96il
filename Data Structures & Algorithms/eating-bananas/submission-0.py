class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we are using binary search to "find the fastest speed" but the mechanism for finding it 
        # is whether or not it completes the banana eating in time or not
        low = 1
        high = max(piles)
        fastestSpeed = high

        while low <= high:
            # Finding the middle and using that as our test speed
            k = (low + high) // 2
            total_hours = 0

            # Calculate total hours needed at speed k
            for p in piles:
                total_hours += math.ceil(p / k)

            if total_hours <= h:
                # we beat the time, lets see if we can find a smaller banana
                high = k -1
                fastestSpeed = k
            else:
                low = k + 1

        return fastestSpeed




