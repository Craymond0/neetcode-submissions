class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                stackI, stackT = stack.pop()
                res[stackI] = index - stackI
                
            stack.append((index,temp))
        
        return res
