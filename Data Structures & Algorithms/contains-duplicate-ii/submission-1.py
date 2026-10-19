class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()

        l = 0

        for r in range(len(nums)):
            if r - l > k:
                numSet.remove(nums[l])
                l += 1

            if nums[r] in numSet:
                return True
            
            numSet.add(nums[r])
            
        return False
