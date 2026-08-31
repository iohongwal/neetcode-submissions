class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
             for j in range(len(num2) - 1, -1, -1):
                num1_i = ord(num1[i]) - ord('0')
                num2_j = ord(num2[j]) - ord('0')
                product = num1_i * num2_j
                position = i + j + 1

                total = product + res[position]

                res[position] = total % 10
                res[position - 1] += total // 10

        return "".join(map(str, res)).lstrip("0")


