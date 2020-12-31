from operator import truediv

class Solution(object):
    def calculator(self, expression):
        index = 0
        return self.__calHelper__(expression, index)[0]

    def __calHelper__(self, expression, index):
        pre, cur, result, sign = 0, 0, 0, '+'
        while index < len(expression):
            char = expression[index]

            if char.isdigit():
                cur = cur * 10 + int(char)                  
            if char in '+-*/' or index == len(expression) - 1 or char == ')':
                
                if sign == '+':
                    result += pre
                    pre = cur
                if sign == '-':
                    result += pre
                    pre = -cur
                if sign == '*':
                    pre *= cur
                if sign == '/':
                    pre = int(truediv(pre,cur))
                cur = 0
                sign = char
            elif char == '(':
                value, index = self.__calHelper__(expression, index+1)
                result += -value if sign == '-' else value
            if sign == ')':
                return result + pre, index
            index += 1
        return (result+pre, index)

print(Solution().calculator('(1 + (2 + (3 + (4 + 5))))'))

print(Solution().calculator('1 - (2 + 3) + 1'))

print(Solution().calculator('21345'))

print(Solution().calculator('14-3/2'))