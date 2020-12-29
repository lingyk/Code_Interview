class solution(object):
    def MetalSurplus(self, costPerCut, salePrice, lengths):
        profit = 0
        maxLen = 0
        for length in lengths:
            maxLen = max(maxLen, length)
        for i in range(1, maxLen+1):
            cut = 0
            piece = 0
            for length in lengths:
                cutCut = (length-1) / i
                cutPiece = length / i
                if i * salePrice - costPerCut * cutCut > 0:
                    cut += cutCut
                    piece += cutPiece
                profit = max(profit, i*salePrice*piece - costPerCut*cut)
            

        return profit
print(solution().MetalSurplus(1, 10, [30,59,110]))
print(solution().MetalSurplus(100, 10, [26,59,103]))
print(solution().MetalSurplus(1, 10, [26,59,103]))