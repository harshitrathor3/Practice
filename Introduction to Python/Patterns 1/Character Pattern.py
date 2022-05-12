## Read input as specified in the question
## Print the required output in given format

n = int(input())

i=1
while i<=n:
    j = 1
    t = i-1
    while j<=i:
        print(chr(t+65), end='')
        t+=1
        j+=1
    i+=1
    print()