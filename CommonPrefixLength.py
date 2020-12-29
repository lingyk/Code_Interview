class solution(object):
    def PrefixLength(self, n):
        size=len(n) #Finding number of strings
        sumlist=[] #Initializing list that'll store sums
        for i in range(size):
            total=0 #Initializing total common prefixes for every string
            string=n[i] #Storing each string in string
            strsize=len(string) #Finding length of each string
            for j in range(strsize):
                suff=string[j:]#Calculating every suffix for a string
                suffsize=len(suff) #Finding length of each suffix
                common=0 #Size of common prefix for each length
                for k in range(suffsize):
                    if(string[k]==suff[k]):
                        common=common+1
                    else:
                        break #If characters at equal positions are not equal, break
                total=total+common #Update total for every suffix
            sumlist.append(total) #Add each total in list
        return sumlist #Return list
            

            

print(solution().PrefixLength(['abcabcd']))
