
import sys

def intersections(arr1, n, arr2, m):
    t=0
    for i in range(n):
        for j in range(m):
            # print(i, j)
            if arr1[i]==arr2[j] and arr1[i]!=-1:
                # ans+=[arr1[i]]
                t+=1
                print(arr1[i], end=' ')
                # arr1[i]=-1
                arr2[j]=-1
                break
    



#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1
