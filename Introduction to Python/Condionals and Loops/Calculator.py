# Write your code here
while True:
    n = int(input())
    if n==6:
        break
    elif n<1 or n>5:
        print('Invalid Operation')
    else:
        a = int(input())
        b = int(input())
        # ans=0
        if n==1:
            ans = a+b
        elif n==2:
            ans = a-b
        elif n==3:
            ans=a*b
        elif n==4:
            ans=a//b
        else:
            ans=a%b
        print(ans)