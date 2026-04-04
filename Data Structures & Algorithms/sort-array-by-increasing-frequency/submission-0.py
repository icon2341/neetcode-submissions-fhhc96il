from collections import Counter
import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        res = []

        temp = []

        for num in count:
            heapq.heappush(temp,(count[num], -num))

        
        while temp:
            tup = heapq.heappop(temp)
            for i in range(tup[0]):
                res.append(-tup[1])

        return res
        