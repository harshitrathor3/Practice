n = int(input())

i=1
while i<=n:
    j=1
    t1, t2 = 1, i
    while j<=2*n:
        if j<=i:
            print(t1, end='')
            t1+=1
        elif 2*n-j<=i-1:
            print(t2, end='')
            t2-=1
        else:
            print(' ', end='')
        j+=1
    i+=1
    print()