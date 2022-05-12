# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):
    if n<=1:
        return -2**31
    m1=m2=-2**31
    for i in arr:
        
        if i>m1:
            m2 = m1
            m1 = i
        elif i>m2 and i!=m1:
            m2=i
        
        #print(i, m1, m2)
    if m1==m2:
        return -2**31
    return m2



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1