import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements in the min-heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        # If we exceed size k, remove the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of a min-heap of size k is the kth largest element
        return self.heap[0]
        
