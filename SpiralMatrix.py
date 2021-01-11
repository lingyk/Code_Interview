class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        cols = len(matrix[0])
        rows = len(matrix)
        seen = [[0] * cols for _ in range (rows)]       
        
        ans = []
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r, c, di = 0, 0, 0
        for _ in range(cols * rows):
            ans.append(matrix[r][c])
            seen[r][c] = 1
            rr, cc = r + dr[di], c + dc[di]
            
            if 0 <= rr < rows and 0 <= cc < cols and seen[rr][cc] == 0:
                r, c, = rr, cc
            else:
                di = (di + 1) % 4
                r, c, = r + dr[di], c + dc[di]
        return ans

print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

print(Solution().spiralOrder([[0]]))
