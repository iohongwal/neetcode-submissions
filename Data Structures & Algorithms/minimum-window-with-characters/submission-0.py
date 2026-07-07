class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resHash, targetHash = {}, {}
        for c in t:
            targetHash[c] = targetHash.get(c, 0) + 1

        l = 0
        res = [-1, -1]
        minLenght = len(s) + 1 
        have, need = 0, len(targetHash)

        for r in range(len(s)):
            c = s[r]
            resHash[c] = 1 + resHash.get(c, 0)

            if c in targetHash and resHash[c] == targetHash[c]:
                have += 1

            while have == need:
                #update our result
                if (r - l + 1) < minLenght:
                    res = [l, r]
                    minLenght = (r - l + 1)
                #pop from the Left of our window
                resHash[s[l]] -= 1
                if s[l] in targetHash and resHash[s[l]] < targetHash[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1] + 1] if minLenght != len(s) + 1 else ""