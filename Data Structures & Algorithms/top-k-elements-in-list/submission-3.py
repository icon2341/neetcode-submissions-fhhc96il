class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we know K is going to be at most the len(nums)
        # we know that we are grouping numbers together based on their frequency
        # and that the number of groups will be < len(nums)
        # so if we make an array where the index is the magnitutde the group
        # represents with the array extending into len(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        # could use counter here if we wanted or default dict
        freqMap = {}

        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        for num in freqMap:
            index = freqMap[num]
            buckets[index].append(num)

        print("Buckets: ", buckets)

        output = []

        kCounter = k
        cursor = len(buckets)-1
        while(kCounter > 0):
            bucketEval = buckets[cursor]

            if(len(bucketEval) == 0):
                cursor -=1
                continue
            
            output.append(buckets[cursor].pop())

            kCounter = kCounter - 1

        return output
