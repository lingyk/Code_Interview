class solution(object):
    def Janitor(self, weight):
        trip = 0
        i = 0
        j = len(weight) - 1
        weight.sort()
        while i <= j:
            trip += 1
            if weight[i] + weight[j] <= 3:
                i += 1
            j -= 1

        return trip
print(solution().Janitor([1.01, 1.99, 2.5, 1.5, 1.01]))