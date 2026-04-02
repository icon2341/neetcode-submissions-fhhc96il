class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalArray = []


        n1 = 0
        n2 = 0

        while(n1 < len(nums1) and n2 < len(nums2)):
            if(nums1[n1] < nums2[n2]):
                finalArray.append(nums1[n1])
                n1 += 1
            else:
                finalArray.append(nums2[n2])
                n2 += 1

        while(n1 < len(nums1)):
            finalArray.append(nums1[n1])
            n1+=1
        while(n2 < len(nums2)):
            finalArray.append(nums2[n2])
            n2+=1

        print(finalArray)
        print(len(finalArray))
        medianIndex = len(finalArray)//2
        print(medianIndex)
        median = finalArray[medianIndex]

        if(len(finalArray) % 2 == 0):
            median = (finalArray[medianIndex] + finalArray[medianIndex-1]) /2


        return median