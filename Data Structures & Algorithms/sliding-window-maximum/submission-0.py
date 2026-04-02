import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Store (-value, index) so we can use min-heap as max-heap
        # and check if the max element is still within the window range
        max_heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(max_heap)
        
        output = [-max_heap[0][0]]
        
        # for value i, itterate through nums every k values
        for i in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            
            # Remove the top of the heap if it's outside the window [i-k+1, i]
            # ah cuz we dont CARE if its not at the top so we only need to remove
            # the top most heap
            # basically, if the index is not supposed to be in our group then we dont consider it
            # and remove it from messing up future calculations
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            # append that value to our output.
            output.append(-max_heap[0][0])
            
        return output
