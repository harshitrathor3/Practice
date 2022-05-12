## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i=1
t = n//2+1
t1 = n//2+1
while i<=n//2+1:
    j=1
    while j<=t:
        if j>=t1:
            print('*', end='')
        else:
            print(' ', end='')
        j+=1
    print()
    t1-=1
    t+=1
    i+=1

i=1
t = n-1
t1 = 1
while i<=n//2:
    j=1
    while j<=t:
        if j>t1:
            print('*', end='')
        else:
            print(' ', end='')
        j+=1
    print()
    i+=1
    t1+=1
    t-=1