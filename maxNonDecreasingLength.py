# go as minimum as possible
# dp1[i] = the longest subarray from 0th to ith index in nums1
# dp1[i] = t11 or t21
# t11 = dp[i-1]+1 if condition else dp[i-1]
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        res, dp1, dp2 = 1, [0]*len(nums1), [0]*len(nums2)
        dp1[0], dp2[0] = 1, 1
        for i in range(1, len(nums1)): 
            t11 = dp1[i-1]+1 if nums1[i]>=nums1[i-1] else 1
            t21 = dp2[i-1]+1 if nums1[i]>=nums2[i-1] else 1
            t12 = dp1[i-1]+1 if nums2[i]>=nums1[i-1] else 1
            t22 = dp2[i-1]+1 if nums2[i]>=nums2[i-1] else 1
            dp1[i] = max(t11, t21)
            dp2[i] = max(t12, t22)
            res = max(res, dp1[i], dp2[i])
        return res
