class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}

        if len(t) != len(s):
            return False


        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)
            tMap[t[i]]  = 1 + tMap.get(t[i] , 0)
        for l in sMap:
            if sMap[l] != tMap.get(l):
                return False
        return True

