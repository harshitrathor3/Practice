## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
k=1

for i in range(1, 2*n):
    t = n-1
    for j in range(1, 2*n):
        if i>1 and j!=1 and j!=2*n and i<2*n-1:
            print(t, end='')
            if j<k:
                t-=1
            if j>=2*n-k:
                t+=1
        else:
            print(n, end='')
    print()
    k+=1