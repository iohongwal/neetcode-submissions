class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_counter = {}
        length = 0
        L = 0

        for R in range(len(s)):
            #Add letter to hashmap 
            letter_counter[s[R]] = letter_counter.get(s[R], 0) + 1
            #find the most letter
            maxCounter = max(letter_counter.values())

            #While the window is invalid, shtink from the left
            while (R - L + 1) - maxCounter > k:
                letter_counter[s[L]] -= 1
                L += 1

            length = max(length, R - L + 1)

        return length


                

