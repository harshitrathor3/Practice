## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

i = 1
while i<=n:
    j = n - i + 1
    t = 1
    while j>=1:
        print(t, end='')
        j-=1
        t+=1
    print()
    i+=1