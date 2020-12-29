class solution(object):
    def slowestKey(self, keyTimes):
        maxDiff = keyTimes[0][1]
        res = chr(ord('a') + keyTimes[0][0])
        for i in range (len(keyTimes)-1):
            nextKey = keyTimes[i+1]
            curKey = keyTimes[i]
            diff = nextKey[1] - curKey[1]
            if diff > maxDiff:
                maxDiff = diff
                res = chr(ord('a')+ nextKey[0])
        
        return res

print(solution().slowestKey([[0,2],[1,5],[0,9],[2,15]]))
print(solution().slowestKey([[0,1],[0,3],[4,5],[5,6],[4,10]]))