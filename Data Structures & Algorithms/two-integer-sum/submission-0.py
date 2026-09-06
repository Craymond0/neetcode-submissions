class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numToIndex:
                return [numToIndex[diff], i]     

            numToIndex[nums[i]] = i 