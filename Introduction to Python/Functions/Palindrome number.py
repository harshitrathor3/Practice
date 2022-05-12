def checkPalindrome(num):
    t = num
    s=0
    while num!=0:
        s += num%10
        num//=10
        s*=10
    s//=10
    return s==t
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
