import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mag_heap = []

        for point in points:
            x = (point[0] - 0) ** 2
            y = (point[1] - 0) ** 2
            magnitude = math.sqrt(x+y)
            heapq.heappush(mag_heap, (magnitude, point))

        output = []
        for i in range(k):
            output.append(heapq.heappop(mag_heap)[1])

        return output