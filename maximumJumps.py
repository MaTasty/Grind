# jump further iff abs(future-current)<=target
# return the max num of jumps to last position; DP
# dp[i] = the max jumps to reach ith index
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [-1]*len(nums)
        dp[0] = 0
        for j in range(1, len(nums)): 
            for i in range(0, j): 
                if abs(nums[j]-nums[i])<=target and dp[i]!=-1: 
                    dp[j] = max(dp[i]+1, dp[j])
        return dp[-1]
