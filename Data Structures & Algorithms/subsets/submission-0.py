class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #we know max num of outcomes is 2 ** len(nums)
        res = []

        # what index are we evaluating
        # what is the path up till that index
        def backtrack(index, path):
            # if we have taken a look at all numbers 
            # in this path
            if(index == len(nums)):
                res.append(path[:])
                return
            
            # decision 1 append the number to the path
            # and backtrack
            path.append(nums[index])
            backtrack(index+1,path)

            # we pop to simply remove this number we added
            # from the path to isolate the two branches from
            # eachother
            path.pop()


            # decision 2, dont add this number to path
            # move on 
            backtrack(index+1, path)

        backtrack(0,[])

        return res
