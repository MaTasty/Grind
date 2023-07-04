# 0/1 knapsack problem; take the paid painter
# 1d array, backwards
# dp[j] = min (dp[j] (without the ith cost), dp[j-time[i]-1 or 0] (with the ith cost )) applies the free painter to time[i] prior to the current wall

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = [float("inf")]*(len(cost)+1)
        dp[0] = 0
        for c, t in zip(cost, time): 
            for j in range(len(dp)-1, 0, -1): 
                dp[j] = min(dp[j], c + dp[max(j-t-1, 0)])
        return dp[-1]
