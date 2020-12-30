class solution(object):
    def findPythagoreanTri(self, nums):
        for a in nums:
            for b in nums:
                for c in nums:
                    if pow(a,2) + pow(b,2) == pow(c,2):
                        return True
        return False

    def findPythagoreanTri2(self, nums):
        square = set([n*n for n in nums])
        print(square)
        for a in nums:
            for b in nums:
                if a*a + b*b in square:
                    return True
        return False

print(solution().findPythagoreanTri2([3,5,12,5,13]))

print(solution().findPythagoreanTri2([0,1,2,3,4,5]))
#0, 1, 4, 9, 16, 25