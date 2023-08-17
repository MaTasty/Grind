# 1. BFS/DFS recursion 
# 2. DP for row and col
# for every row, if 0, then 0; else, min of neighbors plus one
# do the same for each col, only checking 
# forwards and backwards
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowN, colN = len(mat), len(mat[0])
        result = [[float("inf")]*colN for i in range(rowN)]
        for i in range(0, rowN): 
            for j in range(colN): 
                if mat[i][j] == 0: 
                    result[i][j] = 0
                else: 
                    if i-1>=0: 
                        result[i][j] = min(result[i][j], result[i-1][j]+1)
                    if j-1>=0: 
                        result[i][j] = min(result[i][j], result[i][j-1]+1)
        for i in range(rowN-1, -1, -1): 
            for j in range(colN-1, -1, -1): 
                if mat[i][j] == 0: 
                    result[i][j] = 0
                else: 
                    if i+1<rowN: 
                        result[i][j] = min(result[i][j], result[i+1][j]+1)
                    if j+1<colN: 
                        result[i][j] = min(result[i][j], result[i][j+1]+1)

        return result
