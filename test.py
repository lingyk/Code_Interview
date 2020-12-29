string = 'abcabcd'
num = ''
for i in range(len(string)):   
    num = num + string[i]
    #suffix = string[i+1:]
    for j in range(len(num)):
        suffix = string[j:]
        for k in range(len(suffix)):

            if num[j] == suffix[j]:
                print(num)
            else:
                break