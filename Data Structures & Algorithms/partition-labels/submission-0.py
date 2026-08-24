class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res= []

        lastIndex = {}
        size = 0
        end = 0

        for i in range(len(s)):
            lastIndex[s[i]] = i 

        for i in range(len(s)):
        
            end = max(end, lastIndex[s[i]])
            size += 1 

            if i == end:
                res.append(size)
                size = 0
                end = 0
        return res
        
             

