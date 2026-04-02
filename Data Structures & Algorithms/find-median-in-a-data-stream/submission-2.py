import heapq

class MedianFinder:

    def __init__(self):
        # right side
        self.minheap = []
        # left side
        self.maxheap = []

    def addNum(self, num: int) -> None:
        # negative cuz max heap, default operation if empty
        if(len(self.maxheap) == 0):
            heapq.heappush(self.maxheap, -num)
        else:
            # determine which heap to put our num in
            if(num < -self.maxheap[0]):
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        
        # check to see if we are too unbalenced
        if(abs(len(self.maxheap) - len(self.minheap)) > 1):
            # if they are then pop the larger tree and put it in the smaller tree
            if(len(self.maxheap) > len(self.minheap)):
                steal = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -steal)
            else:
                steal = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -steal)

    def findMedian(self) -> float:
        # if the two trees are equal in size, peek both and calc average
        # otherwise peek the larger (odd) tree and just return that val as med
        if(len(self.maxheap) == len(self.minheap)):
            peakmax = -self.maxheap[0]
            peakmin = self.minheap[0]

            return (peakmax + peakmin) /2
        else:
            if(len(self.maxheap) > len(self.minheap)):
                return -self.maxheap[0]
            else:
                return self.minheap[0]

        