## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())

i = 1
while i<=n:
    j = 1
    while j<=i:
        print(chr(64+i), end='')
        j+=1
    print()
    i+=1