class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row is less than the one before
        row = 0
        while(row < len(matrix)):
            print(row)
            low = 0
            high = len(matrix[0]) -1

            while(low <= high):
                print(low,high)
                mid = (low+high)//2
                val = matrix[row][mid]
                if(val == target):
                    return True

                if(target < val):
                    high = mid - 1
                else:
                    low = mid +1

            row += 1

        return False