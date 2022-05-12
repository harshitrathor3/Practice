## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i=1
t=2*n+1
while i<=n:
    j=1
    while j<=2*n+1:
        if j==i or j==n+1 or j==t:
            print('*', end='')
        else:
            print('0', end='')
        j+=1
    t-=1
    i+=1
    print()