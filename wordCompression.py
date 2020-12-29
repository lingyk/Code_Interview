class solution(object):
    def wordCompress(self, word, k):
        wordComp = []

        for char in word:
            if wordComp and wordComp[-1][0] == char:
                wordComp[-1][1] += 1
                if wordComp[-1][1] == k:
                    wordComp.pop()
            else:
                wordComp.append([char, 1])
        
        output = ''
        for char, count in wordComp:
            output += char * count
        return output

print(solution().wordCompress('abbcccb',3))