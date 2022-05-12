## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n = int(input())
e, o = 0, 0
while n!=0:
    ans=n%10
    if ans%2==0:
        e+=n%10
    else:
        o+=n%10
    n//=10
print(e, o)