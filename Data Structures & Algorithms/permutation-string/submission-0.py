class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = Counter(s1)
        window = Counter()
        L = 0

        for R in range(len(s2)):
            window[s2[R]] += 1
            if R - L + 1 > len(s1):
                window[s2[L]] -= 1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L += 1
            if s1_count == window:
                return True


        return False