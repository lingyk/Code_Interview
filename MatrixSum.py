class solution(object):

    def MatrixSum(self, beforeMatrix):
        nRow = len(beforeMatrix)
        nCol = len(beforeMatrix[0])
        if not beforeMatrix:
            return False
        afterMatrix = [[0 for i in range(nRow+1)] for j in range(nCol+1)]
        for row in range (nRow):
            for col in range (nCol):
                if row == 0 and col == 0:
                    afterMatrix[row][col] = beforeMatrix[row][col]
                elif row == 0:
                    afterMatrix[row][col] = afterMatrix[row][col-1] + beforeMatrix[row][col]
                elif col == 0:
                    afterMatrix[row][col] = afterMatrix[row-1][col] + beforeMatrix[row][col]
                else:
                    afterMatrix[row][col] = afterMatrix[row][col-1] + afterMatrix[row-1][col] - afterMatrix[row-1][col-1] + beforeMatrix[row][col]
        
        
        return afterMatrix

print(solution().MatrixSum([[1,2],[0,1],[1,2]]))