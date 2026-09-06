class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts1, counts2 = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            counts1[s[i]] += 1
            counts2[t[i]] += 1
        
        return counts1 == counts2