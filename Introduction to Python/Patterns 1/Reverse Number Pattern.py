## Read input as specified in the question
## Print the required output in given format

n = int(input())

i=1
while i<=n:
    j = 1
    t = i
    while j<=i:
        print(t, end='')
        t-=1
        j+=1
    i+=1
    print()
        