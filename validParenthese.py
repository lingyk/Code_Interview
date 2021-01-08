class Solution(object):
    def isValid(self, s):
        close = {")":"(" , "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in close:
                element = stack.pop() if stack else '#'
                if close[char] != element:
                    return False
                
            else:
                stack.append(char)
                
        return not stack

print(Solution().isValid('[()]'))