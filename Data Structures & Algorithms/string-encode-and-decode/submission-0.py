class Solution:

    def encode(self, strs: List[str]) -> str:
        n = 0
        encoded = ""

        for s in strs:
            n = len(s)
            encoded = encoded + str(n) + "#" + s
        
        return encoded
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        curr = ""

        if s == "":
            return []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            j = i + length

            res.append(s[i:j])

            i = j

        return res
    
                


