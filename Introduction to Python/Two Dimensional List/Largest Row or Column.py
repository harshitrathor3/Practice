'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
    ri = 0
    s1 = -2**31
    for i in range(nRows):
        if sum(arr[i])>s1:
            s1 = sum(arr[i])
            ri = i
    s2 = -2**31
    ci=0
    for i in range(mCols):
        t = 0
        for j in arr:
            t+=j[i]
        if t>s2:
            s2 = t
            ci = i
    if s1>=s2:
        print('row', ri, s1)
    else:
        print('column', ci, s2)
            


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1