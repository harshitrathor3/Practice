from math import ceil, sqrt


def checkMember(n):
    if n==0:
        return True
    n1, n2 = sqrt(5*n**2+4), sqrt(5*n**2-4)
    if ceil(n1)==n1 or ceil(n2)==n2:
        return True
    return False
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")
