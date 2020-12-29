class solution(object):
    def CompetitiveGaming(self, k, score):
        rank = []
        count = 0
        level = 0
        score = sorted(score, reverse=True)
        for i in range(len(score)):
            if score[i] != score[i-1]:
                rank.append(i+1)
            else: 
                count += 1 
                rank.append(i+1-count)
                if rank[i] < rank[i-1]:
                    rank[i] = rank[i-1]

        for i in range(len(rank)):
            if rank[i] <= k:
               level = level+1
        return level, rank


print(solution().CompetitiveGaming(4, [5,2,2,3,4,2,2]))
print(solution().CompetitiveGaming(4, [2,2,2,3,3,4,4,4,5]))