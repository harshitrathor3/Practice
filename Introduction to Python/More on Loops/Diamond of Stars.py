## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
t=n//2+1
for i in range(n//2+1):
    for j in range(n//2+1+i):
        if j>=t-1:
            print('*', end='')
        else:
            print(' ', end='')
    t-=1
    print()

t=1
for i in range(n//2):
    for j in range(n-i-1):
        if j>=t:
            print('*', end='')
        else:
            print(' ', end='')
    print()
    t+=1