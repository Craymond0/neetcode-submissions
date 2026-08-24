class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        res = []

        while l < r:

            curr_sum = numbers[r] + numbers[l]

            if curr_sum > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        

