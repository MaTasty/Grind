class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        # find the smallest interval 
        result = float("inf")
        nums.sort()
        for i in range(1, len(nums)): 
            result = min(nums[i]-nums[i-1], result)
        return result
