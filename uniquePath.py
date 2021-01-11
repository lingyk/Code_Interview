class Solution(object):
    def uniquePaths(self, m, n):

        map = [[0] * n for _ in range (m)]

        for i in range (m):
            map[i][0] = 1
        for i in range(n):
            map[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                map[i][j] = map[i-1][j] + map[i][j-1]
        return map[-1][-1]

print(Solution().uniquePaths(3,7))

print(Solution().uniquePaths(6,2))