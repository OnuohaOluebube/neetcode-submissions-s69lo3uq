class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r)//2

            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        mid = (l + r) // 2
        targetMatrix = matrix[mid]

        l = 0
        r = len(targetMatrix) - 1

        while l <= r:
            m = (l + r)//2

            if targetMatrix[m] < target:
                l = m + 1
            elif targetMatrix[m] > target:
                r = m - 1
            else:
                return True
        return False




        
            

        