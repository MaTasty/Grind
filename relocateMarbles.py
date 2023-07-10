# make nums a set and traverse movefrom and moveto; 
# if from exists, delete it from the set and append to value into the set
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        mySet = set(nums)
        for f, t in zip(moveFrom, moveTo): 
            if f in mySet: 
                mySet.discard(f)
                mySet.add(t)
        result = list(mySet)
        result.sort()
        return result
