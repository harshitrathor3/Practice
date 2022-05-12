
from sys import stdin


def highestOccuringChar(string):
    arr = [0]*26
    for i in string:
        arr[ord(i)-97]+=1
    return chr(arr.index(max(arr))+97)


	



#main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)