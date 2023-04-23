# rotated sorted arr, find the index of target
# if target left is increasing and 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r: 
            mid = l+(r-l)//2
            if nums[mid]>nums[r]: # left side is sorted
                if target<=nums[mid] and target>=nums[l]: 
                    r = mid
                else: 
                    l = mid+1
            else: # right side is sorted
                if target>nums[mid] and target<=nums[r]: 
                    l = mid+1
                else: 
                    r = mid

        if nums[l]==target: 
            return l
        else: 
            return -1
