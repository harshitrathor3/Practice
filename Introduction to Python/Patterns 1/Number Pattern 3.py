## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

i = 1
# t = 1
while i<=n:
    j = 1
    while j<=i:
        if j==1 or j==i:
            print(1, end='')
        else:
            print(2, end='')
        j+=1
    i+=1
    print()