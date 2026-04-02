import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-stone for stone in stones]
        heapq.heapify(stone_heap)

        while(len(stone_heap) > 1):
            y = heapq.heappop(stone_heap) * -1
            x = heapq.heappop(stone_heap) * -1
            result = 0
            if(y>= x):
                result = y - x
            else:
                result = x - y

            if result:
                heapq.heappush(stone_heap, result * -1)
            
        if(len(stone_heap)):
            return stone_heap[0] * -1
        else:
            return 0
        
