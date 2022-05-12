from sys import stdin

def spiralPrint(mat, nRows, mCols):
    sr = 0
    er = nRows-1
    sc = 0
    ec = mCols-1
    cnt = 0
    for _ in range(nRows+mCols-1):
        # print('h')
        for i in range(sc, ec+1):
            print(mat[sr][i], end=' ')
            cnt+=1
        for j in range(sr+1, er+1):
            print(mat[j][ec], end=' ')
            cnt+=1
        for i in range(ec-1, sc-1, -1):
            print(mat[er][i], end=' ')
            cnt+=1
        for j in range(er-1, sr, -1):
            print(mat[j][sr], end=' ')
            cnt+=1
        sr+=1
        sc+=1
        er-=1
        ec-=1


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1