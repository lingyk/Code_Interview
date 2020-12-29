import math

class solution(object):
    def PrisonBreak(self, n, m, h, v):
        '''
            n: row
            m: col
            h: row []
            v: col []
        '''
        h.sort()
        v.sort()
        current = 2
        maximum_n = 2
        maximum_m = 2
        for i in range(len(h)-1):
            if (h[i+1]-1 == h[i]):
                current = current + 1
                maximum_m = max(current, maximum_m)
            else:
                current = 2
        current = 2
        for i in range(len(v)-1):
            if (v[i+1]-1 == v[i]):
                current = current + 1
                maximum_n = max(current, maximum_n)
            else:
                current = 2
        
        return maximum_m * maximum_n

print(solution().PrisonBreak(3,2,[1,2,3],[1,2]))
print(solution().PrisonBreak(4, 4, [1,4], [1,2]))