


class Solution(object):
    def Validator(self, s):
        sum = 0
        decimal = int(s[2:], 16)
        two_digit = s[:2]
        strdeci = str(decimal)
        for num in strdeci:
            num = int(num)
            sum += num
        if int(two_digit, 16) == sum:
            return 'VALID'
        else:
            return 'INVALID'
        
    
    def deciCal(self, s):

        deci = int(s, 16)
        return str(deci)
        

print(Solution().Validator('1CC0FfEE'))
#print(Solution().deciCal('1CC0FfEE'))
   
    