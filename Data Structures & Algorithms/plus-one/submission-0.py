class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        digits[-1] += 1
        tens = digits[-1] // 10
        digits[-1] %= 10

        for i in range(len(digits) - 2, -1, -1):
            digits[i] += tens
            tens = digits[i] // 10
            digits[i] %= 10
            if tens == 0:
                break

        return [1] + digits if tens != 0 else digits