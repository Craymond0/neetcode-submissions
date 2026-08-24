class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window size - count of the most frequent character <= k

        count = {}

        l = 0
        maxf = 0
        res = 0

        for r in range (len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf <= k:
                res = max(res, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return res
            



