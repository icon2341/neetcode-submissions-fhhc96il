class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        output = []
        for num in nums:
            numFreq[num] = 0

        for num in nums:
            numFreq[num] += 1

        buckets = []
        for num in nums:
            buckets.append([])

        for key in numFreq:
            buckets[numFreq[key]-1].append(key)

        print(buckets)

        kCounter = 0

        for bucket in buckets[::-1]:
            if(len(bucket) == 0):
                continue

            while(kCounter < k and len(bucket) > 0):
                output.append(bucket.pop())
                if(len(output) == k):
                    return output
                
            
            

        

        
            


            
                