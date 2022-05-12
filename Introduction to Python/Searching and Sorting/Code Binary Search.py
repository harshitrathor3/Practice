
from sys import stdin


def binarySearch(arr, n, x) :
    l=0
    u=n-1
    # m=(l+u)//2
    while (l<=u):
        m=(l+u)//2
        # print(l, m)
        if arr[m]==x:
            return m
        elif arr[m]>x:
            u = m-1
        elif arr[m]<x:
            l = m+1
    return -1

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1
