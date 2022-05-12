## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

i=1
t1=n
while i<=n:
    j=1
    t=i
    while j<=n+i-1:
        if j>=t1:
            print(t, end='')
            if j<n:
                t-=1
            elif j>=n:
                t+=1
        else:
            print(' ', end='')
        j+=1
    t1-=1
    i+=1
    print()