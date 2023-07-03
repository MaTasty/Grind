# split array into good subarrays: 
# (next - curr)*(next - curr)
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        result, l, r = 0, 0, 0
        while r<len(nums): 
            while r<len(nums) and nums[r]!=1: 
                r+=1
            if r==len(nums): 
                break
            if result == 0: 
                result = 1
            else:
                result *= (r-l)
                result %= 1000000007
            l = r
            r+=1
