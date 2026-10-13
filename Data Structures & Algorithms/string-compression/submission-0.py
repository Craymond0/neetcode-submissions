class Solution:
    def compress(self, chars: List[str]) -> int:
        k, i = 0, 0

        #k is the write pointer, i is the read
        n = len(chars)
        while i < len(chars):
            chars[k] = chars[i]
            k += 1

            j = i + 1
            while j < n and chars[i] == chars[j]:
                j += 1
            
            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1
                
            i = j
        
        return k