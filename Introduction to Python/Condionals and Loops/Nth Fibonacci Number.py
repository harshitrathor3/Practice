## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
if n==1 or n==2:
    print(1)
else:
    n1=1
    n2=1
    for i in range(n-2):
        t=n2
        n2=n2+n1
        n1=t
    print(n2)

