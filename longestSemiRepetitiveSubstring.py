class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        if len(s)==1: return 1
        result, l, r = 1, 0, 1
        onePairFound = False
        lastOccurance = 0
        while r<len(s): 
            if s[r]!=s[r-1]: 
                r+=1
            else: # s[r]==s[r-1]  
                if not onePairFound: 
                    onePairFound = True
                else: 
                    result = max(result, r-l)
                    l = lastOccurance
                lastOccurance = r
                r+=1
        result = max(result, r-l)
        return result
