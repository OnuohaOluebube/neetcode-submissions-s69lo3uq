class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        newNums = [-n for n in nums]

        heapq.heapify(newNums)

        while k > 1:
            heapq.heappop(newNums)
            k -= 1
        res = heapq.heappop(newNums)
        return -1*(res)

        