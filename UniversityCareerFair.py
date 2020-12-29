class solution(object):
    def CareerFair(self, arrival, duration):
        for i in range(len(duration)):
            duration[i] += arrival[i]
        index = list(range(len(arrival)))
        index.sort(key=lambda i:duration[i])
        hosted = set()
        finishTime = 0
        for i in index:
            if arrival[i] >= finishTime:
                hosted.add(i)
                finishTime = duration[i]
        
        return len(hosted)


print(solution().CareerFair([1,2,3,5],[4,1,1,5]))
print(solution().CareerFair([1,3,3,5,7], [2,2,1,2,1]))
print(solution().CareerFair([1,2,3,5],[4,1,1,5]))