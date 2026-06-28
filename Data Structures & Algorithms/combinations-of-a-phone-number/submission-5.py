class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        alphabets = {}

        #covert digits to alphabet
        for digit in digits:
            alphabet = 97 + (int(digit) - 2) * 3 if int(digit) < 8 else 97 + (int(digit) - 2) * 3 + 1
            alphabets[digit] = chr(alphabet)
            alphabets[digit] += chr(alphabet + 1)
            alphabets[digit] += chr(alphabet + 2)
            if digit == "7" or digit == "9":
                alphabets[digit] += chr(alphabet + 3)

        res, subset = [], []

        def backtrack(i):
            #Basecase
            if i >= len(digits):
                res.append("".join(subset))
                return

            #Pick alphabet
            alphabet = alphabets[digits[i]]
            for c in alphabet:
                subset.append(c)
                backtrack(i + 1)
                subset.pop()
        
        backtrack(0)
        return res