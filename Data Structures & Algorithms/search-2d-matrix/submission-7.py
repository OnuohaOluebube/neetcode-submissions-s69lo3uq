class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r)//2
            targetMatrix = matrix[mid]

            if targetMatrix[0] > target:
                r = mid - 1
            elif targetMatrix[-1] < target:
                l = mid + 1

            else:
                
                break

        
        targetMid = (l + r)//2

        targetMatrix = matrix[targetMid]
        if not targetMatrix:
            return False

        targetl = 0
        targetr = len(targetMatrix) - 1

        while targetl <= targetr:
            mid = (targetl + targetr)//2

            if targetMatrix[mid] > target:
                targetr = mid - 1
            elif targetMatrix[mid] < target:
                targetl = mid + 1
            else:
                return True
        
        return False







            

        