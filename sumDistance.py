# Bumping into each other -> assumming they are ghosts -> the values of final positions does not change
# how to calculate the distance between every pair 
# 1. calculate the final positions and sort the array 
# 2. use prefix sum to calculate the pair distance less than n^2 runtime
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        position = [0]*len(nums)
        for i in range(0, len(nums)): 
            if s[i]=="L": 
                position[i] = nums[i]-d
            else: 
                position[i] = nums[i]+d
        position.sort()
        prefix, result = position[0], 0
        for i in range(1, len(position)): 
            prefix += position[i]
            result += (i+1)*position[i]-prefix
            result %= 1000000007
        return result
