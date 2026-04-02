# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        arrayState = []


        # loop and evaluate every index, sorting what is before
        for i in range(len(pairs)):
            temp = pairs[i]
            j = i - 1 # the value before and beforwards

            # loop backwards from i and check which elements are larger than i
            # contiually swap i with its larger neighbors
            while(j >= 0 and pairs[j].key > pairs[j+1].key):
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                j -= 1

            arrayState.append(pairs[:])

        return arrayState



