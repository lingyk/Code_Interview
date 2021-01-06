class Solution(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(self.matrix)
        self.col = len(self.matrix[0])
    def wordSearch(self, word):
        
        for i in range (self.row):
            if self.searchRight(i, word):
                return True
        
        for i in range (self.col):
            if self.searchBottom(i, word):
                return True

        return False

    def searchRight(self, index, word):
        for i in range (self.row):
            if self.matrix[i][index] != word[i]:
                return False
        return True
    def searchBottom(self, index, word):
        for i in range (self.col):
            if self.matrix[index][i] != word[i]:
                return False
        return True

    def exist(self, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.cols = len(self.matrix[0])
        self.rows = len(self.matrix)
        
        for col in range(self.cols):
            for row in range(self.rows):
                if self.backtracking(row, col, word):
                    return True
                
    def backtracking(self, row, col, word):
        
        if len(word) == 0:
            return True
        
        if row < 0 or row == self.rows or col < 0 or col == self.cols or self.matrix[row][col] != word[0]:
            return False
        
        self.matrix[row][col] = '#'
        ret = False
        for rowMove, colMove in [(1,0),(0,1),(-1,0),(0,-1)]:
            ret = self.backtracking(row+rowMove, col+colMove, word[1:])
            
            if ret:
                break
        self.matrix[row][col] = word[0]
        
        return ret


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(Solution(matrix).wordSearch('FOAM'))
print(Solution(matrix).exist('FOAM'))

