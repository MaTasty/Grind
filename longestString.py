# to not contain AAA or BBB, that means no XZ or ZY
# only have one more x than y or one more y than x
# AABBAABBAABBAB
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y: 
            return 2*x + 2*y + 2*z
        elif x < y: 
            return 4*x + 2 + 2*z
        else: 
            return 4*y + 2 + 2*z
