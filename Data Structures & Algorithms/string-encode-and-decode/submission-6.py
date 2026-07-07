class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodeStr = []
        i = 0
        while i < len(s):
            n = ""
            j = i
            while s[j] != "#":
                n += s[j]
                j += 1
            length = int(n)
            decodeStr.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return decodeStr
