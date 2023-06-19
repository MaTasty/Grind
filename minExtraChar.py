# try every possible combinations by memoization structure
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        mem = [-1]*len(s)
        return self.helper(0, s, set(dictionary), mem)

    def helper(self, index, s, diSet, mem): # min number of extra from index to len(s)
        # base cases 
        if index==len(s): 
            return 0
        if mem[index]!=-1: # we have calculated before
            return mem[index]
        result = float('inf')
        for i in range(index, len(s)): 
            curr = s[index:i+1]
            # if curr exists, o/w
            if curr in diSet: 
                result = min(result, 0 + self.helper(i+1, s, diSet, mem))
            else: 
                result = min(result, (i+1-index) + self.helper(i+1, s, diSet, mem))
        mem[index] = result
        return result
