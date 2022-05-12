## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i=1
t=1
k=1
while i<=n//2+1:
    j=1
    while j<=t:
        if j>=i:
            print('* ', end='')
        else:
            print(' ', end='')
        j+=1
    i+=1
    t+=2
    k+=1
    print()
i-=2
k-=3
t-=3
# print(k)
while i>=1:
    j=1
    while j<=t-1:
        if j<=k:
            print(' ', end='')
        else:
            print('* ', end='')
        j+=1
    print()
    i-=1
    k-=1
    t-=2