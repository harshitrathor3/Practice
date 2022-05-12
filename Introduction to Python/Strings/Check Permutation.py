
from sys import stdin


def isPermutation(string1, string2):
    s1 = [0]*26
    s2 = [0]*26
    for i in string1:
        s1[ord(i)-97]+=1
    for i in string2:
        s2[ord(i)-97]+=1
        #print(i, i1)
    #print(s1, s2)
    return s1==s2
    

#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

