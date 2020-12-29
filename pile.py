class solution(object):
    def pile(self, piles):
        if len(piles) < 2:
            return 0
        piles = sorted(piles, reverse=True)
        step = 0
        for i in range(1, len(piles)):
            
            if piles[i] != piles[i-1]:
                step += i
            else:
                return 0
        return step

print(solution().pile([4,3,2,1]))
