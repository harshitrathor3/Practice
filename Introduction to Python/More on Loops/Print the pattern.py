from math import ceil
n = int(input())

t=1
l=[]
try:

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(t, end=' ')
            t+=1
        if i<=n//2:
            l+=[t]
        print()
        if i<=n//2-1:
            t = t + n
        elif n%2==1 and i==n//2:
            t+=n
        else:
            # print(l)
            t = l.pop()
except:
    pass