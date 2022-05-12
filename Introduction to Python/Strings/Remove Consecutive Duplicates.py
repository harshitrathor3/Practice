
from sys import stdin

def removeConsecutiveDuplicates(string):
    res=string[0]
    for i in range(1, len(string)):
        if string[i-1]!=string[i]:
            res+=string[i]
    return res



	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)