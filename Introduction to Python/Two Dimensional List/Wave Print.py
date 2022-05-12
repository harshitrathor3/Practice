from sys import stdin


def wavePrint(mat, nRows, mCols):
    t=0
    t1 = mat[::-1]
    for i in range(mCols):
        t1 = t1[::-1]
        for j in t1:
            print(j[i], end=' ')
        t+=1



#Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1