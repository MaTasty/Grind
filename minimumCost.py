# make subarray equal at a time
# bigger than the mid point, make equal from the back 
# traverse the array and update the result 
class Solution:
    def minimumCost(self, s: str) -> int:
        result = 0
        for index, l in enumerate(s): 
            if index-1>=0 and l == s[index-1]: 
                continue
            if index>len(s)//2: # from the back
                result += len(s)-index
            else: 
                result += (index-0)
        return result
