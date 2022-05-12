## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

i=1
while i<=n:
    j = 1
    t = n - i
    while j<=i:
        print(chr(65+t), end='')
        t+=1
        j+=1
    i+=1
    print()