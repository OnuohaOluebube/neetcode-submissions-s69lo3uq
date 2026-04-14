class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r)//2

            totalhr = 0

            for p in piles:
                totalhr += math.ceil(p/m)

            if totalhr > h:
                l = m + 1
            else:
                res = min(res,m)
                r = m - 1

        return res





        