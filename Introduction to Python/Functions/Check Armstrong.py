## Read input as specified in the question.
## Print output as specified in the question.

n = input()
p = len(n)

s=0
for i in n:
    s+=int(i)**p

if int(n)==s:
    print('true')
else:
    print('false')