class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newPoints = []
        for x,y in points:
            dist = ((x ** 2) + (y ** 2))
            newPoints.append([dist, x,y])
        
        heapq.heapify(newPoints)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(newPoints)
            res.append([x,y])
            k-=1
        return res



        