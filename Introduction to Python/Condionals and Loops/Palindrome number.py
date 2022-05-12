def checkPalindrome(num):
    s=0
    t=num
    while num!=0:
        s+=num%10
        s*=10
        num//=10
    s//=10
    # print(s, t)
    return t==s
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
