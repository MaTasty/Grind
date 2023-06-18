# keeps tracking of colRemain and rowRemain and rowStatus and colStatus
# if row or col is filled then skip 
# val*the number colRemain or rowRemain and then update the colRemain and rowRemain
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowRemain, colRemain, rowStatus, colStatus = n, n, [False]*n, [False]*n
        result = 0
        for i in range(len(queries)-1, -1, -1): 
            typeC, index, val = queries[i]
            if typeC == 0: # fill a row
                if rowStatus[index]: 
                    continue
                result += val*colRemain
                rowStatus[index] = True
                rowRemain -= 1
            else: # fill a col
                if colStatus[index]:
                    continue
                result += val*rowRemain
                colStatus[index] = True
                colRemain -= 1
        return result
