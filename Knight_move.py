class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #(row, col)

        visited = [(0, 0)]
        count = [(0, 0, 0)]
        x, y = abs(x), abs(y)
        while visited:
            step = 0      
            path = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2),
                   (-2, 1), (1, -2), (2, -1)]
            a, b, step = count.pop(0)
            if (a, b) == (x, y):
                return step
            for dx, dy in path:
                na = a + dx #next a 
                nb = b + dy #next b
                if (na, nb) not in visited and na >= 0 and nb >= 0: 
                    visited.append((a+dx, b+dy))
                    count.append((a+dx, b+dy, step+1))
        return False

print (Solution().minKnightMoves(5, 5))


