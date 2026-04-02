import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num_heap = []

        for num in nums:
            heapq.heappush(num_heap, num)
            if(len(num_heap) > k):
                heapq.heappop(num_heap)
        return heapq.heappop(num_heap)