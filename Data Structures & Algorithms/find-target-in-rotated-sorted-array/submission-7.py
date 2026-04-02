class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while(low <= high):
            mid = (low + high) //2
            print((low, nums[low]),(mid,nums[mid]), (high,nums[high]))
            if(nums[mid] == target):
                return mid
            if(nums[low] <= nums[mid]):
                # then we know left is sorted
                if(target < nums[low] or target > nums[mid]):
                    # go right
                    low = mid+1
                else:
                    # go left
                    high = mid-1
            else:
                # right is sorted
                if(target > nums[high] or target < nums[mid]):
                    # go left
                    high = mid-1
                else:
                    # go right
                    low = mid+1
        return -1

