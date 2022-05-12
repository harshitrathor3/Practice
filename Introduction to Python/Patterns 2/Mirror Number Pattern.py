## Read input as specified in the question
## Print the required output in given format

n = int(input())
i = 1
while i<=n:
    j = 1
    t = 1
    while j<=n:
        if j>=n-i+1:
            print(t, end='')
            t+=1
        else:
            print(' ', end='')
        j+=1
    print()
    i+=1