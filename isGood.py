# a permutation of nay array base[n]: 1 to n-1 + n + n
# 1. if the len is n+1 n as the max
# 2. Sort and traverse
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums)!=max(nums)+1 or len(nums)==1: 
            return False
        nums.sort()
        for i in range(1, len(nums)-1): 
            if nums[i]!=1 and nums[i-1]+1!=nums[i]: 
                return False
        if nums[-1]!=nums[-2]: 
            return False
        return True
