class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Use floor division to find the center index
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid # Found it! The index is correct relative to the original list.
            
            if target > nums[mid]:
                low = mid + 1  # Toss out the left half
            else:
                high = mid - 1 # Toss out the right half
                
        return -1 # Target isn't in the list