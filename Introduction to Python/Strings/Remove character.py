
from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	return string.replace(ch, '')




	

#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)