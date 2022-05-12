
from sys import stdin


def reverseEachWord(string):
    ans = ''
    for i in string.split(' '):
        ans+=i[::-1]+' '
    return ans





#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)