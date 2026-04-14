class Solution:
    def findMin(self, nums: List[int]) -> int:
     
        l, r = 0, len(nums) - 1
        res = nums[l]
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l] 
                
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1
    
        return res

            
            
            


        