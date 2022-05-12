#Write Your Code Here
'''n = input()
if n[0]=='0':
    print('0'*len(n))
n = int(n)
while n!=0:
    ans = n%10
    if ans!=0:
        print(ans, end='')
    n = n//10'''
n = int(input())

s=0
while n!=0:
    s+=n%10
    s*=10
    n//=10
print(s//10)
