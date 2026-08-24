class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)


        for i in range(len(freq) - 1,0, -1):
    
            for num in freq[i]:
                res.append(num)
                k -= 1

            if k == 0:
                return res

        return res