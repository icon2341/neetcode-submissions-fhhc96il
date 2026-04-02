class Solution:
    def search(self, nums: List[int], target: int) -> int:
            low = 0
            high = len(nums) - 1

            while low <= high:
                m = (low + high) // 2
                
                if nums[m] == target:
                    return m

                # Identify the sorted half
                if nums[low] <= nums[m]:  # Left side is sorted
                    if nums[low] <= target < nums[m]: # Target is in the left side
                        high = m - 1
                    else: # Target is in the right side
                        low = m + 1
                else:  # Right side is sorted
                    if nums[m] < target <= nums[high]: # Target is in the right side
                        low = m + 1
                    else: # Target is in the left side
                        high = m - 1
                        
            return -1