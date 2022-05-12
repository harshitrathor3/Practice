n = int(input())
i = 1

while i<=n:
    j=n+i-1
    t=i
    t1=1
    while j>=1:
        if t1>=n-i+1:
            print(t, end='')
            t1-=1
            if j>=i+1:
                t+=1
            else:
                t-=1
        else:
            print(' ', end='')
        j-=1
        t1+=1
    i+=1
    print()